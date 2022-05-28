from django.urls import path

from sisys.sisis_auth.views import UserLoginView, UserLogoutView, RegisterUser, profile_details, \
    PassChangeDoneView, PassResetView, PassResetDoneView, PassChangeView, AccountView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile_details, name='profile details'),
    path('account/', AccountView.as_view(), name='my account'),
    path('change-password/', PassChangeView.as_view(), name='change password'),
    path('change-password-done/', PassChangeDoneView.as_view(), name='change password done'),
    path('reset-password/', PassResetView.as_view(), name='reset password'),
    path('reset-password-done/', PassResetDoneView.as_view, name='reset password done'),
)
