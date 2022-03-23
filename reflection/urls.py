from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormReflectionView.as_view(), name="home"),
    path('dashboard/', views.dashboard_view, name='dashboard')
]