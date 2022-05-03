import calendar
from datetime import date, datetime, timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from django.views import View, generic
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .choices import FEELING_ICONS
from .forms import FormReflectionOne, FormReflectionTwo
from .models import DailyQuote, ReflectionEntry
from .serializers import ReflectionEntrySerializer
from .utils import ReflectionCalendar

# Create your views here.


class FormReflectionView(View):
    form_class = [FormReflectionOne, FormReflectionTwo]
    template_name = ["reflection/form1.html", "reflection/form2.html"]

    def get(self, request, *args, **kwargs):
        return self.render_formOne(request)

    def post(self, request, *args, **kwargs):
        if request.POST.get("ReflectionForm1"):
            return self.render_formOne(request)

        if request.POST.get("ReflectionForm2"):
            form1 = self.form_class[0](request.POST)
            if not form1.is_valid():
                return self.render_formOne(request)
            request.session["Data_ReflectionForm1"] = form1.cleaned_data.get("feeling")
            feeling = request.session["Data_ReflectionForm1"]
            return self.render_formTwo(request, feeling)

        if request.POST.get("submit"):
            return self.submit(request)

    def render_formOne(self, request):
        form1 = self.form_class[0]()
        quote = DailyQuote.get_quote()
        if request.user.is_authenticated:
            request.user.profile.update_streak()
        return render(
            request,
            self.template_name[0],
            {"form1": form1, "icons": FEELING_ICONS, "quote": quote},
        )

    def render_formTwo(self, request, feeling):
        form2 = (
            FormReflectionTwo(
                initial=request.session["Data_ReflectionForm2"], feeling=feeling
            )
            if "Data_ReflectionForm2" in request.session
            else FormReflectionTwo(feeling=feeling)
        )
        adjective_choices = form2.get_adjectives(feeling=feeling)
        reason_choices = form2.get_reasons
        update = request.user.is_authenticated and ReflectionEntry.get_entries(request.user, date=datetime.now()).exists()
        feeling_words = ["very sad", "sad", "neutral", "happy", "very happy"]
        return render(
            request,
            self.template_name[1],
            {
                "form2": form2,
                "feeling": feeling_words[int(feeling) - 1],
                "adjective_choices": adjective_choices,
                "reason_choices": reason_choices,
                "update": update,
            },
        )

    def submit(self, request):
        feeling = request.session["Data_ReflectionForm1"]
        form2 = FormReflectionTwo(feeling=feeling, data=request.POST)
        if not form2.is_valid():
            return self.render_formTwo(request, feeling)
        if request.user.is_authenticated:
            data_form2 = form2.cleaned_data
            feeling = request.session["Data_ReflectionForm1"]
            adjective = data_form2.get("adjective")
            reason = data_form2.get("reason")
            if ReflectionEntry.get_entries(request.user, date=datetime.now()).exists():
                ReflectionEntry.get_entries(
                    request.user, date=datetime.now()
                ).update(feeling=feeling, adjective=adjective, reason=reason, deleted=False)
                messages.success(request, "Reflection Updated Successfully")
            else:
                request.user.profile.update_streak(True)
                ReflectionEntry.objects.create(
                    user=request.user,
                    feeling=feeling,
                    adjective=adjective,
                    reason=reason,
                    deleted=False,
                )
                messages.success(request, "Reflection Saved Successfully")
        else:
            messages.error(request, "You're not logged in, reflection did not save")

        return redirect("dashboard")

class ReflectionEntryDetail(APIView):
    serializer = ReflectionEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, user, pk):
        try:
            return ReflectionEntry.get_entry(user, pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        entry = self.get_object(request.user, pk)
        serializer = self.serializer(entry)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        entry = self.get_object(request.user, pk)
        entry.delete_entry()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReflectionEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ReflectionEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ReflectionEntry.get_entries(self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        finalized_response = ReflectionEntry.choicenumbers_to_text(serializer.data)
        return Response(finalized_response)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete_entry()

class DashboardView(LoginRequiredMixin, generic.ListView):
    login_url = "/accounts/login"
    redirect_field_name = "dashboard"
    model = ReflectionEntry
    template_name = "reflection/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get("month", None))
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        cal = ReflectionCalendar(d.year, d.month)

        entries = ReflectionEntry.get_entries(
            user=self.request.user, date__year=d.year, date__month=d.month
        )

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(entries=entries, today=date.today(), withyear=True)
        context["calendar"] = mark_safe(html_cal)
        return context

# Function for Dashboard_View
def get_date(req_day):
    if req_day:
        year, month = map(int, req_day.split("-"))
        return date(year, month, day=1)
    return datetime.now()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month
