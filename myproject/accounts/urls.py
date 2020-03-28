from django.urls import path
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

urlpatterns = [
    path("register",views.register,name="register"),
    path("register/",views.register,name="register"),
    path('login',views.login,name="login"),
    path('login/',views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path('password-reset/', views.passwordResetEmail, name='password_reset_email'),
    path('password-reset/done/', views.passwordResetEmailSent, name='password_reset_email_done'),
    path('reset/<uidb64>/<token>/', views.passwordReset, name='password_reset'),
    path('reset/done/', views.passwordResetDone, name='password_reset_done'),

]