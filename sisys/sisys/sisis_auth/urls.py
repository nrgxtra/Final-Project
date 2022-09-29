from django.urls import path

from sisys.sisis_auth.views import UserLoginView, UserLogoutView, RegisterUser, profile_details, AccountView, \
    PassChangeView, PassChangeDoneView, PassResetView, PassResetDoneView, PassConfirmationView, PassResetComplete, \
    EmailConfirmationView, activate, delete_account

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile_details, name='profile details'),
    path('account/', AccountView.as_view(), name='my account'),
    path('change-password/', PassChangeView.as_view(), name='change password'),
    path('change-password-done/', PassChangeDoneView.as_view(), name='change password done'),
    path('reset-password/', PassResetView.as_view(), name='reset_password'),
    path('reset-password-done/', PassResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PassConfirmationView.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/', PassResetComplete.as_view(), name='password_reset_complete'),
    path('email-confirmation', EmailConfirmationView.as_view(), name='email_confirm'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('delete/', delete_account, name='delete_account'),
)
