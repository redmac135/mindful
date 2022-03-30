import calendar
import requests
import pytz
from datetime import datetime, date, timedelta
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.utils.timezone import localtime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from .models import ReflectionEntry, DailyQuote
from .forms import FormReflectionOne, FormReflectionTwo
from .utils import ReflectionCalendar
from .choices import FEELING_ICONS
from mindful.settings import ZENQUOTES_API_KEY
from django.contrib import messages

from .serializers import ReflectionEntrySerializer
from rest_framework import viewsets, permissions
from rest_framework.utils import serializer_helpers

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
            form1 = self.form_class[0](request.POST)
            if not form1.is_valid():
                return self.render_formOne(request)
            request.session['Data_ReflectionForm1'] = form1.cleaned_data.get('feeling')
            feeling = request.session['Data_ReflectionForm1']
            return self.render_formTwo(request, feeling)

        if request.POST.get('submit'):
            return self.submit(request)

    def render_formOne(self, request):
        form1 = self.form_class[0]()
        date_cst = localtime(timezone=pytz.timezone('US/Central')).date()
        if DailyQuote.objects.filter(date = date_cst).exists():
            obj = DailyQuote.objects.get(date = date_cst)
            quote = {'quote': obj.quote, 'author': obj.author}
        else:
            quote = self.get_quote(date_cst)
        return render(request, self.template_name[0], {'form1': form1, 'icons': FEELING_ICONS, 'quote': quote})

    def render_formTwo(self, request, feeling):
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
        feeling = request.session['Data_ReflectionForm1']
        form2 = FormReflectionTwo(feeling=feeling, data=request.POST)
        if not form2.is_valid():
            return self.render_formTwo(request, feeling)
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
                messages.success(request, 'Reflection Updated Successfully')
            else:
                ReflectionEntry.objects.create(
                    user=request.user,
                    feeling=feeling,
                    adjective=adjective,
                    reason=reason,
                )
                messages.success(request, 'Reflection Saved Successfully')
        else:
            messages.error(request, 'You\'re not logged in, reflection did not save')
            
        return redirect('dashboard')
    
    def get_quote(self, date_cst):
        url = 'https://zenquotes.io/api/today/' + ZENQUOTES_API_KEY
        response = requests.get(url).json()[0]
        quote = response['q']
        author = response['a']
        DailyQuote.objects.create(
            date = date_cst,
            quote = quote,
            author = author,
        )
        return {'quote': quote, 'author': author}

class ReflectionEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ReflectionEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReflectionEntry.objects.filter(user=self.request.user)
    
    def finalize_response(self, request, response, *args, **kwargs):
        if type(response.data) == serializer_helpers.ReturnList:
            finalized_response = []
            for item in response.data:
                finalized_response.append(ReflectionEntry.choicenumbers_to_text(item))
        else:
            finalized_response = ReflectionEntry.choicenumbers_to_text(response.data)

        response.data = finalized_response
        return super().finalize_response(request, response, *args, **kwargs)

class DashboardView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login'
    redirect_field_name = 'dashboard'
    model = ReflectionEntry
    template_name = 'reflection/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        cal = ReflectionCalendar(d.year, d.month)

        entries = ReflectionEntry.objects.filter(
            user=self.request.user,
            date__year=d.year, 
            date__month=d.month
        )

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(entries=entries, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

# Function for Dashboard_View
def get_date(req_day):
    if req_day:
        year, month = map(int, req_day.split('-'))
        return date(year, month, day=1)
    return datetime.now()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
