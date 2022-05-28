from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages

# Create your views here.


class AboutUsView(TemplateView):
    template_name = "about/about_us.html"
