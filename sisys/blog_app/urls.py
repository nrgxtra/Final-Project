from django.urls import path

from blog_app.views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView, BlogSearchView, \
    post_like, \
    posts_with_tag, author_posts

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post_details'),
    path('post-create/', PostCreateView.as_view(), name='post_create'),
    path('post-update/<int:pk>/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    path('search-blog', BlogSearchView.as_view(), name="search_blog"),
    path('like/<int:pk>/<slug:slug>', post_like, name='like'),
    path('posts-tag/<tag>', posts_with_tag, name='posts_with_tag'),
    path('author-posts/<author>', author_posts, name='author_posts'),
]
