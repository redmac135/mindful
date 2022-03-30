from django import forms


class FAQForm(forms.Form):
    question = forms.CharField(label="Question", max_length=300)
