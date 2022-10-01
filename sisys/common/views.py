from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog_app.models import Post
from common.forms import BookingForm
from common.models import Service, Category


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def show_about(request):
    resent_posts = Post.objects.all()[:3]
    services = Service.objects.all()[:3]
    context = {
        'resent_posts': resent_posts,
        'services': services,
    }
    return render(request, 'common/about.html', context)


class ServicesView(ListView):
    model = Service
    template_name = 'common/services.html'
    context_object_name = 'services'
    paginate_by = 3


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'common/service-details.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context


def list_services_by_category(request, cat):
    filtered = Service.objects.filter(category__name__icontains=cat).all()

    context = {
        'service_category': filtered,
    }
    return render(request, 'common/service-categories.html', context)


def make_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

