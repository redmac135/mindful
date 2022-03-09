from django import forms
from .models import ReflectionEntry, AdjectiveChoice
from .choices import FEELING_CHOICES, REASON_CHOICES

class FormReflectionOne(forms.Form):
    feeling = forms.ChoiceField(choices=FEELING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = ReflectionEntry
        fields = ['feeling']

class FormReflectionTwo(forms.Form):
    def __init__(self, feeling, *args, **kwargs):
        super(FormReflectionTwo, self).__init__(*args, **kwargs)
        self.fields['adjective'].choices = AdjectiveChoice.getChoices(feeling)
    
    adjective = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple)
    reason = forms.MultipleChoiceField(choices=REASON_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ReflectionEntry
        fields = ['adjective', 'reason', ]