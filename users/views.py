from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import SignUpForm
from .models import Profile

# Create your views here.
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'email': user.email, 'token': user.token})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() # Create User in Default User Model
            user.refresh_from_db()

            # Add Profile Attributes to User Object
            user.email = form.cleaned_data.get('email')
            user.token = form.cleaned_data.get('token')

            # Create Profile Object
            update_user_data(user)

            # Login to Newly Created User
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})