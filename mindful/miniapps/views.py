from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BreathingView(TemplateView):
    template_name = "miniapps/breathing.html"