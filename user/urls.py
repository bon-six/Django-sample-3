from django.urls import path

from .views import Homepage, UserTokenLoginView
from .views import UserRegister, UserVerification, UserRegisterAPI

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('api-token-login/', UserTokenLoginView.as_view(), name='token_login'),
    path('accounts/register/', UserRegister.as_view(), name='register'),
    path('accounts/verify/<uidb64>/<token>', UserVerification.as_view(), name='verify_acc'),
    path('accounts/apiregister/', UserRegisterAPI.as_view(), name='apiregister'),
]
