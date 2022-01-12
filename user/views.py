from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import serializers

from .models import MyUser
from .admin import UserCreationForm

# Create your views here.
class AccountProfile(generic.TemplateView, generic.base.TemplateResponseMixin):
    content_type = "application/json"
    template_name = 'user/profile.json'

class Homepage(generic.TemplateView, generic.base.TemplateResponseMixin):
    content_type = "application/json"
    template_name = 'user/home.json'
'''
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email','password' ]
    
    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'], validated_data['password'])
        return user

class UserRegister(CreateAPIView):
    permission_classes = (AllowAny,)
    #queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
'''
class UserRegister(generic.CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('profile')

class UserVerification(generic.View):
    model = MyUser
    def get(self, request, *args, **kwargs):
        try: 
            user = MyUser.objects.get(pk=kwargs['pk'])
            user.is_active = True
            user.save()
        except MyUser.DoesNotExist:
            pass

        return HttpResponse("user verification done")