from django.shortcuts import render

from blog_app.models import Post
from common.models import Service


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def show_about(request):
    resent_posts = Post.objects.all()[:3]
    context = {
        'resent_posts': resent_posts,
    }
    return render(request, 'common/about.html', context)


def show_services(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'common/services.html', context)
