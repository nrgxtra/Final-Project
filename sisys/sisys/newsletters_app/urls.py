from django.urls import path

from sisys.newsletters_app.views import newsletter_signup, newsletter_signout

urlpatterns = (
    path('up/', newsletter_signup, name='newsletter signup'),
    path('out/', newsletter_signout, name='newsletter signout'),
)
