from django.urls import path
from . import views

urlpatterns = [
    path('', views.reflection_formview, name="reflection"),
    path('dashboard/', views.dashboard_view, name='dashboard')
]