from django.urls import path
from .views import BreathingView

urlpatterns = [
    path('', BreathingView.as_view(), name="breathing"),
]