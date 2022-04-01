from django import forms
from .models import Question


class QuestionForm(forms.Form):
    email = forms.EmailField()
    question = forms.CharField(label="Question", max_length=300)

    class Meta:
        model = Question
        fields = ['email', 'question', ]
