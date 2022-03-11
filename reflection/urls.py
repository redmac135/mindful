from django.urls import path
from . import views

urlpatterns = [
    path('', views.reflection_formview, name="home"),
    path('dashboard/', views.dashboard_view, name='dashboard')
]