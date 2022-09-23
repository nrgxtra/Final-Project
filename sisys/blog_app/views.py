from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

from .forms import CommentForm, PostCreationForm
from .models import Post, Comment, Like


class HomeView(ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

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
        comments = post.comment_set.all()
        likes = post.like_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        context['likes'] = likes
        context['user'] = user
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


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'blog/post-create.html'
    permission_required = 'blog.can_create'

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


class SearchView(ListView):
    model = Post
    template_name = 'blog/tags.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET['query']
        posts = Post.objects.filter(title__icontains=query)
        context['query'] = query
        context['posts'] = posts

        return context

    paginate_by = 6


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
