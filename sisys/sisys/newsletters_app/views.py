from django.shortcuts import render, redirect

from sisys.newsletters_app.forms import NewsletterUserSignUpForm


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'newsletter/news-sign-up.html', context)


def newsletter_signout(request):
    pass
