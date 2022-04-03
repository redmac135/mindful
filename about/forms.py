from django import forms
from .models import Question

# TODO: get email directly from logged in user
# TODO: only allow question to be submitted if user is logged in
class QuestionForm(forms.Form):
    email = forms.EmailField()
    question = forms.CharField(label="Question", max_length=300)

    class Meta:
        model = Question
        fields = ['email', 'question', ]
