from django.urls import path

from common.views import show_about, show_services

urlpatterns = [
    path('about/', show_about, name='about'),
    path('services/', show_services, name='services'),

]
