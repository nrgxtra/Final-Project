from django.urls import path

from blog_app.views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView, SearchView, post_like

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post_details'),
    path('post-create/', PostCreateView.as_view(), name='post_create'),
    path('post-update/<int:pk>/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    path('search', SearchView.as_view(), name="search"),
    path('like/<int:pk>/<slug:slug>', post_like, name='like'),
]
