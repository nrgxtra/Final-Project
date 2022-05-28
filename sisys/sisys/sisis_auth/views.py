import django.contrib.auth.views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import django.views.generic as views

from sisys.blog_app.models import Post
from sisys.sisis_auth.forms import RegisterForm, ProfileForm, PasswordChangeForm
from sisys.sisis_auth.models import Profile


class RegisterUser(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('profile details')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('profile details')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = 'home'


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
        return render(request, 'accounts/my-account.html', context)
    user_posts = Post.objects.filter(author_id=request.user.id)
    context = {
        'form': form,
        'posts': user_posts,
        'profile': profile,
    }
    return render(request, 'accounts/my-account.html', context)


class PassChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('change password done')


class PassChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password-change-done.html'


class PassResetView(auth_views.PasswordResetView):
    pass


class PassResetDoneView(auth_views.PasswordResetDoneView):
    pass
