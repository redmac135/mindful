from django import forms

import re

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LogInForm(AuthenticationForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user_object = User.objects.get(username=username)
                profile = Profile.objects.get(user=user_object)
                if profile.email_confirmed == False:
                    raise ValidationError('Please confirm your email before signing in. Be sure to also check your spam folder for the email')

        return super(LogInForm, self).clean()

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if username and email:
            # Check Username and Email Uniqueness
            if User.objects.filter(username=username).exists():
                raise ValidationError({'username': "An Account with this Username Already Exists"})
            if User.objects.filter(email=email).exists():
                raise ValidationError({'email': "An Account with this Email Already Exists"})

        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        labels = {'email': 'K12 Email', }

class ResendActivationEmailForm(forms.Form):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')

        if email:
            if not User.objects.filter(email=email).exists():
                raise ValidationError({'email': "An Account with this Email Address does not Exist"})
            user = User.objects.get(email=email)
            profile = Profile.objects.get(user=user)
            if profile.email_confirmed == True:
                raise ValidationError({'email': "Your Email is Already Active!"})
            check_last_sent = profile.check_last_sent(timezone.now())
            if not check_last_sent == True:
                formated_time = check_last_sent.strftime("%A %I:%M:%S %p")
                raise ValidationError({'email': f"You can only send one confirmation email every 12 hours, the next time you can send an email is {formated_time}"})
                
        return cleaned_data