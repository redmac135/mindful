from tkinter import W
from django import forms
from .models import ReflectionEntry

FEELING_CHOICES = (
    (1, 'Very Sad'),
    (2, 'Sad'),
    (3, 'Neutral'),
)

ADJECTIVE_CHOICES = (
    (1, 'Happy'),
    (2, 'Confident'),
    (3, 'Excited'),
)

REASON_CHOICES = (
    (1, 'Family'),
    (2, 'Friends'),
    (3, 'Work'),
    (4, 'School'),
)

class FormReflectionOne(forms.Form):
    feeling = forms.ChoiceField(choices=FEELING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = ReflectionEntry
        fields = ['feeling']

class FormReflectionTwo(forms.Form):
    adjective = forms.MultipleChoiceField(choices=ADJECTIVE_CHOICES, widget=forms.CheckboxSelectMultiple)
    reason = forms.MultipleChoiceField(choices=REASON_CHOICES, widget=forms.CheckboxSelectMultiple)
    rose = forms.CharField(max_length=500)
    bud = forms.CharField(max_length=500)
    thorn = forms.CharField(max_length=500)

    class Meta:
        model = ReflectionEntry
        fields = ['adjective', 'reason', 'rose', 'bud', 'thorn']