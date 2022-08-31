from django.urls import path

from newsletters_app.views import newsletter_signup, newsletter_signout, UnsubscribeSuccessView

urlpatterns = (
    path('up/', newsletter_signup, name='newsletter signup'),
    path('out/', newsletter_signout, name='newsletter signout'),
    path('unsub-success/', UnsubscribeSuccessView.as_view(), name='unsubscribe success'),
)

from .signals import *

