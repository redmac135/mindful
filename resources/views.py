from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class ResourcesView(TemplateView):
    template_name = "resources/resources.html"
