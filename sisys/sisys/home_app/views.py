from django.shortcuts import render
import django.views.generic as views

from sisys.sisis_auth.models import Profile


class HomeView(views.TemplateView):
    template_name = 'index.html'


def show_gallery(request):
    return render(request, 'gallery-1.html')
