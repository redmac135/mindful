from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegistrationToken
 
class SignUpForm(UserCreationForm):
    def clean_token(self):
        if not RegistrationToken.objects.filter(token=self).exists():
            raise ValidationError("This token doesn't exist, check your spelling")
        else:
            regtoken = RegistrationToken.objects.get(token=self)
            if not regtoken.valid:
                raise ValidationError("This token is no longer valid.")
        return self

    email = forms.EmailField(required=True)
    token = forms.CharField(max_length=9, required=True, validators=[clean_token])

    class Meta:
        model = User
        fields = ('username', 'email', 'token', 'password1', 'password2', )
        labels = {'email': 'Email', 'token': 'Registration Token', }