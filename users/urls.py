from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import SignUpView, ActivateAccountView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('', include('django.contrib.auth.urls'))
]