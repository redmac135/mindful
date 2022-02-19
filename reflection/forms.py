from django import forms
from .models import ReflectionEntry
from .choices import FEELING_CHOICES, REASON_CHOICES

class FormReflectionOne(forms.Form):
    feeling = forms.ChoiceField(choices=FEELING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = ReflectionEntry
        fields = ['feeling']

class FormReflectionTwo(forms.Form):
    def __init__(self, adjective_choices, *args, **kwargs):
        super(FormReflectionTwo, self).__init__(*args, **kwargs)
        self.fields['adjective'].choices = adjective_choices

    adjective = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple)
    reason = forms.MultipleChoiceField(choices=REASON_CHOICES, widget=forms.CheckboxSelectMultiple)
    rose = forms.CharField(max_length=500)
    bud = forms.CharField(max_length=500)
    thorn = forms.CharField(max_length=500)

    class Meta:
        model = ReflectionEntry
        fields = ['adjective', 'reason', 'rose', 'bud', 'thorn']