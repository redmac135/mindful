from django.shortcuts import render

from django.views.generic import View
from .models import Resource

# Create your views here.


class ResourcesView(View):
    template_name = "resources/resources.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "resource_types": Resource.ResourceType.choices,
                "resources": Resource.objects.all(),
            },
        )
