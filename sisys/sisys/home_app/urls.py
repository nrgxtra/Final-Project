
from django.urls import path

from sisys.home_app.views import show_gallery, HomeView

urlpatterns = (
    # path('', show_home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('gallery/', show_gallery, name='gallery'),
)
