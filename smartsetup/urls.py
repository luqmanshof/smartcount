from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.admin import AdminSite

# admin.site.site_url = 'localhost'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('list_signup',views.list_signup,name='list_signup'),
    path('signup/edit',views.edit_signup,name='edit_signup'),

    # path('admin/',admin.site.urls),

    path('password_change',auth_views.PasswordChangeView.as_view(template_name='registration/change_password_form.html'),name='password_change'),
    path('password_change_success',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_success.html'),name='password_change_success'),
    # path('smartsetup/password',auth_views.PasswordChangeView.as_view(template_name='registration/change_password_form.html'),name='password'),

    path('password_reset',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_page.html'),name='password_reset'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_success.html'),name='password_reset_done'),
    path('password_reset_confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_sure.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_completed.html'),name='password_reset_complete'),

    path('login',auth_views.LoginView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
]
