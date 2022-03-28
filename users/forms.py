import re

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            # Checking Email Valid
            pattern_domain = r'^[a-zA-Z0-9._-~]+@(ycdsbk12)\.ca$'
            pattern = r'^[a-zA-Z]+\.[a-zA-Z]+(\d{0}|\d{2})@(ycdsbk12)\.ca$'
            if not re.match(pattern_domain, email):
                raise ValidationError({'email': "Please signup with your ycdsbk12 email"})
            elif not re.match(pattern, email):
                raise ValidationError({'email': 'Please enter a valid ycdsbk12 email'})

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