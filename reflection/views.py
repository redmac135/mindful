from datetime import datetime, date
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import ReflectionEntry
from .forms import FormReflectionOne, FormReflectionTwo
from .utils import ReflectionCalendar
from .choices import FEELING_ICONS

# Create your views here.

class FormReflectionView(View):
    form_class = [FormReflectionOne, FormReflectionTwo]
    template_name = ['reflection/form1.html', 'reflection/form2.html']

    def get(self, request, *args, **kwargs):
        return self.render_formOne(request)

    def post(self, request, *args, **kwargs):
        if request.POST.get('ReflectionForm1'):
            return self.render_formOne(request)
        if request.POST.get('ReflectionForm2'):
            return self.render_formTwo(request)
        if request.POST.get('submit'):
            return self.submit(request)

    def render_formOne(self, request):
        form1 = self.form_class[0]()
        return render(request, self.template_name[0], {'form1': form1, 'icons': FEELING_ICONS})

    def render_formTwo(self, request):
        form1 = self.form_class[0](request.POST)
        if not form1.is_valid():
            return self.render_formOne(request)
        request.session['Data_ReflectionForm1'] = form1.cleaned_data.get('feeling')
        feeling = request.session['Data_ReflectionForm1']
        form2 = (
            FormReflectionTwo(
                initial=request.session['Data_ReflectionForm2'], feeling=feeling
            )
            if 'Data_ReflectionForm2' in request.session
            else FormReflectionTwo(feeling=feeling)
        )

        adjective_choices = form2.get_adjectives(feeling=feeling)
        reason_choices = form2.get_reasons
        if request.user.is_authenticated:
            update = bool(
                ReflectionEntry.objects.filter(
                    user=request.user, date=datetime.now()
                ).exists()
            )
        else: 
            update = False

        return render(request, self.template_name[1], {'form2': form2, 'feeling': feeling, 'adjective_choices': adjective_choices, 'reason_choices':reason_choices, 'update': update})

    def submit(self, request):
        form2 = FormReflectionTwo(feeling = request.session['Data_ReflectionForm1'], data=request.POST)
        if not form2.is_valid():
            return self.render_formTwo(request)
        if request.user.is_authenticated:
            data_form2 = form2.cleaned_data
            feeling = request.session['Data_ReflectionForm1']
            adjective = data_form2.get('adjective')
            reason = data_form2.get('reason')
            if ReflectionEntry.objects.filter(
                user=request.user, date=datetime.now()
            ).exists():
                ReflectionEntry.objects.filter(
                    user=request.user, date=datetime.now()
                ).update(feeling=feeling, adjective=adjective, reason=reason)

            else:
                ReflectionEntry.objects.create(
                    user=request.user,
                    feeling=feeling,
                    adjective=adjective,
                    reason=reason,
                )
            return redirect('dashboard')
        return redirect('home')

@login_required
def dashboard_view(request):
    d = get_date(request.GET.get('day', None))
    cal = ReflectionCalendar(d.year, d.month)
    entries = ReflectionEntry.objects.filter(date__year=d.year, date__month=d.month, user=request.user)
    html_cal = cal.formatmonth(entries, withyear=True)

    return render(request, 'reflection/dashboard.html', {'calendar': mark_safe(html_cal)})

# Function for Dashboard_View
def get_date(req_day):
    if req_day:
        year, month = map(int, req_day.split('-'))
        return date(year, month, day=1)
    return datetime.now()
