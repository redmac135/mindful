from django.shortcuts import render
from django.views.generic import TemplateView, View

from .forms import FAQForm

# Create your views here.


class AboutUsView(TemplateView):
    template_name = "about/about_us.html"


class FAQView(View):
    template_name = "about/faq.html"
    form_class = FAQForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})
