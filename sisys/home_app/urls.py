
from django.urls import path

from home_app.views import HomeView, show_gallery

urlpatterns = (
    # path('', show_home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('gallery/', show_gallery, name='gallery'),
)
