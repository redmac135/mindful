from django.shortcuts import render

from django.views.generic import View
from .models import Resource

# Create your views here.


class ResourcesView(View):
    template_name = "resources/resources_form.html"

    def get(self, request):
        t = request.GET.get("t", "")
        if t == "all":
            print(Resource.objects.all())
            return render(
                request,
                "resources/resources_list.html",
                {"resources": Resource.objects.all()},
            )
        if t in {"hotlines", "counselling", "cbt"}:
            return render(
                request,
                "resources/resources_list.html",
                {"resources": Resource.objects.filter(resource_t=t)},
            )
        return render(request, self.template_name)
