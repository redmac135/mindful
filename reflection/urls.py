from django.urls import path
from . import views

urlpatterns = [
    path('', views.reflection_view, name="home"),
]