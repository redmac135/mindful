from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import Profile
from .forms import SignUpForm, ResendActivationEmailForm
from django.contrib.auth.models import User
from django.views.generic import View

from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token

# Create your views here.

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'users/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            Profile.send_activation_email(user, request)
            messages.success(request, ('Please Confirm your email to complete registration.'))

            return redirect('login')

        return render(request, self.template_name, {'form': form})

class ActivateAccountView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.profile.email_confirmed = True
            user.profile.save()
            messages.success(request, ('Your account have been confirmed.'))
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('login')

class ResendActivationEmailView(View):
    form_class = ResendActivationEmailForm
    template_name = 'users/resend_activation_email.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data.get('email')

            user = User.objects.get(email=email)

            Profile.send_activation_email(user, request)
            messages.success(request, ('Activation Email Successfully Sent.'))

            return redirect('login')

        return render(request, self.template_name, {'form': form})