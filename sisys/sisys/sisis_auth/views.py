import django.contrib.auth.views as auth_views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import django.views.generic as views
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from sisys.blog_app.models import Post
from sisys.sisis_auth.forms import RegisterForm, ProfileForm
from sisys.sisis_auth.models import Profile
from sisys.sisis_auth.utils import generate_token
from sisys.sisis_auth.utils import send_activation_mail
User = get_user_model()


class RegisterUser(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('email_confirm')

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        user = self.object
        send_activation_mail(self.request, user)
        return result


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Now You can log on to Your account')
        return redirect('login')
    else:
        return render(request, 'accounts/activation-failed.html', {'user': user})


class EmailConfirmationView(views.TemplateView):
    template_name = 'accounts/activate-your-account.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('profile details')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = 'home'


class AccountView(LoginRequiredMixin, views.TemplateView):
    template_name = 'accounts/my-account.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(pk=self.request.user.id)
        self.extra_context = {'profile': profile, }
        return super().get_context_data(**kwargs)


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'accounts/profile_details.html', context)
    user_posts = Post.objects.filter(author_id=request.user.id)
    context = {
        'form': form,
        'posts': user_posts,
        'profile': profile,
    }
    return render(request, 'accounts/profile_details.html', context)


class PassChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('change password done')


class PassChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password-change-done.html'


class PassResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password-reset.html'


class PassResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password-reset-complete.html'


class PassConfirmationView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password-reset-confirm.html'


class PassResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password-reset-done.html'
