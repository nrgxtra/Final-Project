from django.urls import path

from sisys.newsletters_app.views import newsletter_signup, newsletter_signout, UnsubscribeSuccessView, send_newsletter

urlpatterns = (
    path('up/', newsletter_signup, name='newsletter signup'),
    path('out/', newsletter_signout, name='newsletter signout'),
    path('unsub-success/', UnsubscribeSuccessView.as_view(), name='unsubscribe success'),
    path('send-news/', send_newsletter, name='send-newsletter'),
)
