from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='reflection'),
    path('dashboard/', views.dashboard_view, name='dashboard')
]