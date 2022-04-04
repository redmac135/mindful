from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages

from .models import Question, DefaultQuestion
from .forms import QuestionForm

# Create your views here.


class AboutUsView(TemplateView):
    template_name = "about/about_us.html"


class FAQView(View):
    template_name = "about/faq.html"
    form_class = QuestionForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form, "questions": DefaultQuestion.objects.all()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data.get('email')
            question = cleaned_data.get('question')

            if request.user.is_authenticated:
                Question.objects.create(
                    user=request.user,
                    email=email,
                    question=question
                )
            else:
                Question.objects.create(
                    email=email,
                    question=question
                )
            messages.success(request, ('Question sent successfully, we\'ll get back to you soon'))
            return redirect('home')
        return render(request, self.template_name, {"form": form})
