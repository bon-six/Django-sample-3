from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail


from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import serializers

from .models import MyUser
from .admin import UserCreationForm


class Homepage(generic.TemplateView, generic.base.TemplateResponseMixin):
    content_type = "application/json"
    template_name = 'user/home.json'

class UserTokenLoginView(generic.TemplateView):
    template_name = 'user/token_login.html'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email','password' ]
    
    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'], validated_data['password'])
        request = self.context.get('request')
        message = render_to_string("user/acc_activate_email.txt", {
            'user':user,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_mail("Acc email verification", message, 'admin@apitask.web', [validated_data['email']])
        return user

class UserRegisterAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    #queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class UserRegister(generic.CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'user/register_acc.html'
    success_url = reverse_lazy('home')

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            message = render_to_string("user/acc_activate_email.txt", {
                'user':user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_mail = form.cleaned_data.get('email')
            send_mail("Acc email verification", message, 'admin@apitask.web', [to_mail])
            return JsonResponse({'message':'Please verify your email to finish the registration process.'})

class UserVerification(generic.View):
    model = MyUser
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = MyUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return JsonResponse({'message':'Thank you for your email confirmation. Now you can login your account.'})
        else:
            return JsonResponse({'message':'Activation link is invalid!'})
