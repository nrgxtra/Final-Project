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
from shopping_app.utils import get_user_subscription
from sisys.sisis_auth.models import SisisUser
from .forms import CommentForm, PostCreationForm
from .mixins import GroupRequiredMixin
from .models import Post, Comment, Like, Tag
from .utils import get_author_name, get_author_bio


class HomeView(ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    paginate_by = 4

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        resent_posts = self.queryset[:3]
        user = self.request.user
        tags = Tag.objects.all()
        subscribed_user = get_user_subscription(user)
        if user.is_authenticated:
            customer, created = Customer.objects.get_or_create(user=user)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_quantity
            context['user'] = user
            context['tags'] = tags
            context['resent_posts'] = resent_posts
            context['cart_items'] = cart_items
            context['subscribed_user'] = subscribed_user

            return context
        else:
            cart_items = 0
            context['user'] = user
            context['tags'] = tags
            context['resent_posts'] = resent_posts
            context['cart_items'] = cart_items
            context['subscribed_user'] = subscribed_user

            return context


class PostView(DetailView):
    model = Post
    template_name = "blog/post-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]
        user = self.request.user
        subscribed_user = get_user_subscription(user)

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
        context['subscribed_user'] = subscribed_user
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
        user = self.request.user
        subscribed_user = get_user_subscription(user)

        context = super().get_context_data(**kwargs)
        context['form'] = form
        context['subscribed_user'] = subscribed_user
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
        subscribed_user = get_user_subscription(self.request.user)
        update = True
        context['update'] = update
        context['subscribed_user'] = subscribed_user

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
        subscribed_user = get_user_subscription(self.request.user)
        context['subscribed_user'] = subscribed_user
        context['posts'] = posts

        return context


def posts_with_tag(request, tag):
    user = request.user
    subscribed_user = get_user_subscription(user)
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_quantity
    else:
        cart_items = '0'
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
        'cart_items': cart_items,
        'resent_posts': resent_posts,
        'paginator': paginator,
        'subscribed_user': subscribed_user,

    }
    return render(request, 'blog/tags.html', context)


def author_posts(request, author):
    user = request.user
    subscribed_user = get_user_subscription(user)
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.get_cart_quantity
    else:
        cart_items = '0'
    author = SisisUser.objects.filter(email=author).first()
    if not author:
        context = {
            'cart_items': cart_items,
            'subscribed_user': subscribed_user,
        }
        return render(request, 'blog/no-author.html', context)
    author_id = author.id
    tags = Tag.objects.all()
    posts = Post.objects.filter(author_id=author_id)
    name = get_author_name(author)
    bio = get_author_bio(author)
    fb_link = author.profile.fb_link
    vm_link = author.profile.vimeo_link
    tw_link = author.profile.tweeter_link
    link_link = author.profile.link_link
    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'author': author,
        'bio': bio,
        'fb': fb_link,
        'vm': vm_link,
        'tw': tw_link,
        'link': link_link,
        'name': name,
        'tags': tags,
        'cart_items': cart_items,
        'page_obj': page_obj,
        'paginator': paginator,
        'subscribed_user': subscribed_user,
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
