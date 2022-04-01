from django.urls import path

from .views import AboutUsView, FAQView

urlpatterns = [
    path("", AboutUsView.as_view(), name="about_us"),
    path("faq/", FAQView.as_view(), name="faq"),
]
