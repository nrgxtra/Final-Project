from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from blog_app.models import Post
from common.forms import BookingForm, ContactForm
from common.models import Service, Category, Appointment, GalleryPicks
from common.utils import send_appointment_confirmation_mail, send_appointment_to_staff, send_question_to_staff
import asyncio

loop = asyncio.get_event_loop()


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def show_about(request):
    resent_posts = Post.objects.all()[:3]
    services = Service.objects.all()[:3]
    gallery = GalleryPicks.objects.all()[:8]
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = f"name: {form.cleaned_data['name']} email: {form.cleaned_data['email']} phone: {form.cleaned_data['phone_number']} for date:{form.cleaned_data['date']} message: {form.cleaned_data['message']}"
            loop.run_in_executor(None, send_appointment_confirmation_mail, email)
            loop.run_in_executor(None, send_appointment_to_staff, message)
            form.save()
            return redirect('booking_success')
    form = BookingForm
    context = {
        'resent_posts': resent_posts,
        'services': services,
        'picks': gallery,
        'form': form,
    }
    return render(request, 'common/about.html', context)


class BookingSuccess(TemplateView):
    template_name = 'common/booking-success.html'


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
            email = form.cleaned_data['email']
            message = f"name: {form.cleaned_data['name']} email: {form.cleaned_data['email']} phone: {form.cleaned_data['phone_number']} for date:{form.cleaned_data['date']} message: {form.cleaned_data['message']}"
            loop.run_in_executor(None, send_appointment_confirmation_mail, email)
            loop.run_in_executor(None, send_appointment_to_staff, message)
            form.save()
            return redirect('booking_success')
        else:
            errors = form.errors
            context = {
                'form': form,
                'errors': errors,
            }
            return render(request, 'common/appointment.html', context)
    form = BookingForm
    context = {
        'form': form,
    }
    return render(request, 'common/appointment.html', context)


class GalleryView(ListView):
    template_name = 'common/gallery.html'
    model = GalleryPicks
    context_object_name = 'gallery_picks'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_pics = GalleryPicks.objects.all()[:6]
        context['recent_pics'] = recent_pics
        return context


class FaqView(TemplateView):
    template_name = 'common/faq.html'


class TermsView(TemplateView):
    template_name = 'common/terms-condition.html'


class PrivacyView(TemplateView):
    template_name = 'common/privacy-policy.html'


def send_question(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = f"name: {form.cleaned_data['name']} email: {form.cleaned_data['email']} phone: {form.cleaned_data['phone_number']} subject:{form.cleaned_data['subject']} message: {form.cleaned_data['message']}"
            loop.run_in_executor(None, send_question_to_staff, message)
            form.save()
            return redirect('question_sent')
    form = ContactForm
    errors = form.errors
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, 'common/contact.html', context)


class QuestionSentView(TemplateView):
    template_name = 'common/question-sent.html'

