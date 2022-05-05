from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import localtime
from multiselectfield import MultiSelectField

import requests
import random
import pytz
from datetime import date

from mindful.settings import ZENQUOTES_API_KEY
from .choices import *

CHOICES_LIST = [ADJECTIVE_CHOICES_1, ADJECTIVE_CHOICES_2, ADJECTIVE_CHOICES_3, ADJECTIVE_CHOICES_4, ADJECTIVE_CHOICES_5]

CHOICES_LIST_DICT = [dict(x) for x in CHOICES_LIST]
REASON_CHOICES_DICT = dict(REASON_CHOICES)

# Create your models here.

class ReflectionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=date.today)
    feeling = models.IntegerField()
    adjective = MultiSelectField(choices=ADJECTIVE_CHOICES, max_choices=3)
    reason = MultiSelectField(choices=REASON_CHOICES, max_choices=3)
    deleted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('entry-detail', args=[str(self.id)])

    @staticmethod
    def get_entries(user, **kwargs):
        return ReflectionEntry.objects.filter(user=user, **kwargs).exclude(deleted=True)

    @staticmethod
    def get_entry(user, pk, **kwargs):
        return ReflectionEntry.objects.filter(user=user, pk=pk, **kwargs).exclude(deleted=True)

    def delete_entry(self):
        self.deleted = True
        self.save()
        return True

    @staticmethod
    def choicenumbers_to_text(data):
        if isinstance(data, list):
            return [ReflectionEntry.choicenumbers_to_text(x) for x in data]

        adjective_list = CHOICES_LIST_DICT[data["feeling"] - 1]
        data["adjective"] = [adjective_list[int(x)] for x in data["adjective"]]
        data["reason"] = [REASON_CHOICES_DICT[int(x)] for x in data["reason"]]

        return data

    def __str__(self):
        return str(self.user) + " " + str(self.date)

    class Meta:
        ordering = ['-date']

class AdjectiveChoice(models.Model):
    feeling = models.IntegerField()
    order = models.IntegerField()
    adjective = models.CharField(max_length=16)

    def getChoices(feeling):
        choices_list = AdjectiveChoice.objects.filter(feeling=feeling)
        choices = [(x.order, x.adjective) for x in choices_list]
        return choices

    def __str__(self):
        return str(self.feeling) + " " + self.adjective

class QuoteResponse(models.Model):
    quote = models.CharField(max_length=256)
    author = models.CharField(max_length=32)
    happysad = models.IntegerField()

    def __str__(self):
        return self.quote

class DailyQuote(models.Model):
    date = models.DateField()
    quote = models.CharField(max_length=256)
    author = models.CharField(max_length=32)

    def get_quote():
        date_cst = localtime(timezone=pytz.timezone("US/Central")).date()
        if DailyQuote.objects.filter(date=date_cst).exists():
            obj = DailyQuote.objects.get(date=date_cst)
            return {"quote": obj.quote, "author": obj.author}
        url = "https://zenquotes.io/api/today/" + ZENQUOTES_API_KEY
        try:
            response = requests.get(url).json()[0]
            quote = response["q"]
            author = response["a"]
        except:
            random_list = list(DailyQuote.objects.all())
            response = random.choice(random_list)
            quote = response.quote
            author = response.author
        DailyQuote.objects.create(
            date=date_cst,
            quote=quote,
            author=author,
        )
        return {"quote": quote, "author": author}

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-date']