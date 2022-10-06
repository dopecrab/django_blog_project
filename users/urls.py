from django.urls import path
from . import views as usr_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', usr_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('profile/', usr_views.profile_settings, name = 'profile-settings' ),
    path('password-reset/', 
    auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'), 
    name = 'password_reset'),
    path('password-reset/done', 
    auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'), 
    name = 'password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'), 
    name = 'password_reset_confirm'),
    path('password-reset/complete', 
    auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'), 
    name = 'password_reset_complete'),
]
