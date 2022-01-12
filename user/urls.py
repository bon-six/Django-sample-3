from django.urls import path

from .views import AccountProfile, Homepage, UserRegister, UserVerification

urlpatterns = [
    path('accounts/profile/', AccountProfile.as_view(), name='profile'),
    path('accounts/register/', UserRegister.as_view()),
    path('accounts/verify/<int:pk>/', UserVerification.as_view()),
    path('',Homepage.as_view(), name='home')
]