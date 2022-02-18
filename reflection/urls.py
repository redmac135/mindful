from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormWizardView.as_view(), name="reflection"),
]