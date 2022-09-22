from django.urls import path

from blog_app.views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post_details'),
    path('post-create/', PostCreateView.as_view(), name='post_create'),
    path('post-update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
