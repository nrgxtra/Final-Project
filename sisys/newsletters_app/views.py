from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from newsletters_app.models import NewsletterUser


@login_required
def newsletter_signup(request):
    if request.method == 'POST':
        sub_user = NewsletterUser(email=request.user.email)
        sub_user.save()
    return redirect('home')


def newsletter_signout(request):
    user_mail = request.user.email
    subscriber = NewsletterUser.objects.all().get(email=user_mail)
    if subscriber:
        if request.method == 'POST':
            subscriber.delete()
            return redirect('unsubscribe success')
        context = {
            'user': subscriber,
        }
        return render(request, 'newsletter/unsubscribe-confirmation.html', context)
    else:
        return render(request, 'newsletter/unsubscribe-error.html')


class UnsubscribeSuccessView(TemplateView):
    template_name = 'newsletter/unsubscribe-success.html'
