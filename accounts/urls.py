from django.urls import path
from . import views
from django.contrib.auth import views  as auth_views
from django.views.decorators.csrf import csrf_exempt
from .views import EmailValidationView, VerificationView,Register,identitycardView




urlpatterns = [

	path('register/', Register.as_view(), name = 'register'),
	path('login/', auth_views.LoginView.as_view(), name = 'login'),
	path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
 	path('emailverify/',views.emaiverify, name='emaiverify'),
    path('validate_email', csrf_exempt(EmailValidationView.as_view()),name='validate_email'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(), name='activate'),  
	path('profile/', views.ProfileView, name = 'profile'),
    path('profile/profile_pdf/', views.identitycardView.as_view(), name = 'profile-pdf'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]
