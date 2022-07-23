from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from sisys.newsletters_app.forms import NewsletterUserSignUpForm
from sisys.newsletters_app.models import NewsletterUser
from sisys.newsletters_app.tasks import send_mail_to_all


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterUserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:

            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'newsletter/news-sign-up.html', context)
    if request.user.is_authenticated:
        sub_user = NewsletterUser(email=request.user.email)
        sub_user.save()
        return redirect('home')
    form = NewsletterUserSignUpForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'newsletter/news-sign-up.html', context)


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


@login_required
def send_newsletter(request):
    context = {
        'user': request.user,
    }
    if request.user.is_superuser:
        if request.method == 'POST':
            send_mail_to_all.delay()
        return render(request, 'newsletter/send-news.html', context)
