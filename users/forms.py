from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, RegistrationToken
 
class SignUpForm(UserCreationForm):  
    def clean(self):
        cleaned_data = self.cleaned_data
        token = cleaned_data.get('token')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Checking Registrating Token Validation
        if not RegistrationToken.objects.filter(token=token).exists():
            raise ValidationError("This token doesn't exist, check your spelling")
        else:
            regtoken = RegistrationToken.objects.get(token=token)
            if not regtoken.valid:
                raise ValidationError("This token is no longer valid.")
            else:
                regtoken.valid = False

        # Check Username and Email Uniqueness
        if User.objects.filter(username=username).exists():
            raise ValidationError("An Account with this Username Already Exists")
        if Profile.objects.filter(email=email).exists():
            raise ValidationError("An Account with this Email Already Exists")

        return cleaned_data

    email = forms.EmailField(required=True)
    token = forms.CharField(max_length=9, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'token', 'password1', 'password2', )
        labels = {'email': 'Email', 'token': 'Registration Token', }