from django.urls import path

from .views import AboutUsView, FAQView

urlpatterns = [
    path("", AboutUsView.as_view(template_name="about/about_us.html"), name="about_us"),
    path("faq/", FAQView.as_view(template_name="about/faq.html"), name="faq"),
]
