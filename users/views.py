from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import SignUpForm
from .models import Profile

# Create your views here.
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'email': user.profile.email, 'token': user.profile.token})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.profile.email = form.cleaned_data.get('email')
            user.profile.token = form.cleaned_data.get('token')
            update_user_data(user)

            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def dashboard_view(request):
    return render(request, 'users/dashboard.html', {})