from django.urls import path
from .views import BreathingView, CoffeeView

urlpatterns = [
    path('breathing', BreathingView.as_view(), name="breathing"),
    path('coffee', CoffeeView.as_view(), name="coffee")
]