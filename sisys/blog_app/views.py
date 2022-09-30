from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from shopping_app.models import Customer, Order
from sisys.sisis_auth.models import SisisUser
from .forms import CommentForm, PostCreationForm
from .mixins import GroupRequiredMixin
from .models import Post, Comment, Like, Tag
from .utils import get_author_name


class HomeView(ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    paginate_by = 4

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        resent_posts = self.queryset[:3]
        user = self.request.user
        tags = Tag.objects.all()
        if user.is_authenticated:
            customer, created = Customer.objects.get_or_create(user=user)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_quantity
            context['user'] = user
            context['tags'] = tags
            context['resent_posts'] = resent_posts
            context['cart_items'] = cart_items

            return context
        else:
            order = {'get_cart_total': 0, 'get_cart_quantity': 0, }
            cart_items = order['get_cart_quantity']
            context['user'] = user
            context['tags'] = tags
            context['resent_posts'] = resent_posts
            context['cart_items'] = cart_items

            return context


class PostView(DetailView):
    model = Post
    template_name = "blog/post-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]
        user = self.request.user

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        tags = [t.name for t in post.tags.all()]
        comments = post.comment_set.all()
        likes = post.like_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        context['likes'] = likes
        context['user'] = user
        context['tags'] = tags
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class PostCreateView(GroupRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'blog/post-create.html'

    def get_context_data(self, **kwargs):
        form = PostCreationForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blog_home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post-update.html'
    fields = ["title", "content", "image", "tags"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blog_home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post-delete.html'

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("blog_home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class BlogSearchView(ListView):
    model = Post
    template_name = 'blog/blog.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        posts = Post.objects.filter(title__icontains=query).all()

        return posts

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()

        context['posts'] = posts

        return context


def posts_with_tag(request, tag):
    posts = Post.objects.filter(tags__name__icontains=tag)
    tags = Tag.objects.all()
    resent_posts = Post.objects.all()[:3]
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'tags': tags,
        'tag': tag,
        'resent_posts': resent_posts,
        'paginator': paginator,

    }
    return render(request, 'blog/tags.html', context)


def author_posts(request, author):
    author = SisisUser.objects.filter(email=author).first()
    author_id = author.id
    tags = Tag.objects.all()
    posts = Post.objects.filter(author_id=author_id)
    name = get_author_name(author)
    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'author': author,
        'name': name,
        'tags': tags,
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'blog/author.html', context)


@login_required
def post_like(request, pk, slug):
    post = Post.objects.get(pk=pk)
    already_liked = post.like_set.filter(user_id=request.user.id).first()
    if already_liked:
        already_liked.delete()
    else:
        like = Like(
            post=post,
            user=request.user,
        )
        like.save()
    return redirect('post_details', post.id, slug)
