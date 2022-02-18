from django.shortcuts import render, redirect
from .models import ReflectionEntry
from .forms import FormReflectionOne, FormReflectionTwo
from formtools.wizard.views import SessionWizardView
from django.contrib import messages

# Create your views here.
class FormWizardView(SessionWizardView):
    template_name = "reflection/form.html"
    form_list = [FormReflectionOne, FormReflectionTwo]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        if self.request.user:
            ReflectionEntry.objects.create(**form_data[1], feeling=form_data[0]['feeling'], user=self.request.user)
            messages.success(self.request, 'Your reflection entry was saved.')
        return redirect('home')