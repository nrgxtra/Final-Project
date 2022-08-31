from django.shortcuts import render
import django.views.generic as views

from newsletters_app.models import NewsletterUser


class HomeView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_active:
            sub_user = NewsletterUser.objects.all().filter(email=self.request.user.email)
            if sub_user:
                context = {
                    'subscribed_user': self.request.user,
                }
                return context
        else:
            context = {
                'user': self.request.user,
            }
            return context


def show_gallery(request):
    return render(request, 'gallery-1.html')
