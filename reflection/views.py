from django.shortcuts import render, redirect
from .models import ReflectionEntry, AdjectiveChoice
from .forms import FormReflectionOne, FormReflectionTwo
from formtools.wizard.views import SessionWizardView
from django.contrib import messages
from .choices import ADJECTIVE_CHOICES_1, ADJECTIVE_CHOICES_2, ADJECTIVE_CHOICES_3, ADJECTIVE_CHOICES_4, ADJECTIVE_CHOICES_5

# Create your views here.

FORMS = [('home', FormReflectionOne), ('reflection', FormReflectionTwo)]

TEMPLATES = {'home': 'reflection/form.html', 'reflection': 'reflection/reflection.html'}

class FormWizardView(SessionWizardView):
    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        if self.request.user:
            ReflectionEntry.objects.create(**form_data[1], feeling=form_data[0]['feeling'], user=self.request.user)
            messages.success(self.request, 'Your reflection entry was saved.')
        return redirect('home')
    
    # attempt at making dynamic choices based on first choice
    def get_form(self, step=None, data=None, files=None):
        if step is None:
            step = self.steps.current

        if step == '1':
            firststep_data = self.get_cleaned_data_for_step('0')
            choices_list = AdjectiveChoice.objects.filter(feeling=firststep_data['feeling'])
            choices = [(x.order, x.adjective) for x in choices_list]
            form = FormReflectionTwo(choices)
        else:
            return super(FormWizardView, self).get_form(step, data, files)
        
        return form
