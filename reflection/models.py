from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from .choices import *

CHOICES_LIST = [ADJECTIVE_CHOICES_1, ADJECTIVE_CHOICES_2, ADJECTIVE_CHOICES_3, ADJECTIVE_CHOICES_4, ADJECTIVE_CHOICES_5]

# Create your models here.

class ReflectionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    feeling = models.IntegerField()
    adjective = MultiSelectField(choices=ADJECTIVE_CHOICES, max_choices=3)
    reason = MultiSelectField(choices=REASON_CHOICES, max_choices=3)
    
    def choicenumbers_to_text(data):
        feeling = data['feeling']
        finalized_adjectives = []
        adjective_list = CHOICES_LIST[feeling-1]
        for adjective in data['adjective']:
            finalized_adjectives.extend(choice[1] for choice in adjective_list if choice[0] == int(adjective))
        finalized_reasons = []
        for reason in data['reason']:
            finalized_reasons.extend(choice[1] for choice in REASON_CHOICES if choice[0] == int(reason))
        data['adjective'] = finalized_adjectives
        data['reason'] = finalized_reasons

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

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-date']