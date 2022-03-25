from django.urls import path
from .views import FormReflectionView, DashboardView

urlpatterns = [
    path('', FormReflectionView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]