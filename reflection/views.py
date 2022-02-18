from django.shortcuts import render
from .models import ReflectionEntry
from .forms import FormReflectionOne, FormReflectionTwo
from formtools.wizard.views import SessionWizardView

# Create your views here.
class FormWizardView(SessionWizardView):
    template_name = "reflection/form.html"
    form_list = [FormReflectionOne, FormReflectionTwo]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ReflectionEntry.objects.create(**form_data[1], feeling=form_data[0]['feeling'])
        return render(self.request, 'home/home.html', {
            'form_data': form_data,
        })