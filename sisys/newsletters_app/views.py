from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from newsletters_app.forms import NewsletterUserSignUpForm
from newsletters_app.models import NewsletterUser


@login_required
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST)
    context = {
        'form': form,
        'name': request.user.email,
    }
    if request.method == 'POST':
        if form.is_valid():
            sub_user = NewsletterUser(email=request.user.email)
            sub_user.save()
            return redirect('home')
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
