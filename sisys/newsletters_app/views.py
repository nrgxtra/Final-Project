from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from newsletters_app.models import NewsletterUser
from shopping_app.utils import get_context_attributes


@login_required
def newsletter_signup(request):
    if request.method == 'POST':
        sub_user = NewsletterUser(email=request.user.email)
        sub_user.save()
    return redirect('home')


def newsletter_signout(request):
    user_mail = request.user.email
    subscriber = NewsletterUser.objects.all().get(email=user_mail)
    context_data = get_context_attributes(request, request.user)
    if subscriber:
        if request.method == 'POST':
            subscriber.delete()
            return redirect('unsubscribe success')
        context = {
            'user': subscriber,
            'cart_items': context_data['cart_items'],
        }
        return render(request, 'newsletter/unsubscribe-confirmation.html', context)
    else:
        return render(request, 'newsletter/unsubscribe-error.html')


class UnsubscribeSuccessView(TemplateView):
    template_name = 'newsletter/unsubscribe-success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context_data = get_context_attributes(self.request, self.request.user)
        context['user'] = user
        context['cart_items'] = context_data['cart_items']
        return context
