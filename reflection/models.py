from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from .choices import ADJECTIVE_CHOICES, REASON_CHOICES

# Create your models here.

class ReflectionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    feeling = models.IntegerField()
    adjective = MultiSelectField(choices=ADJECTIVE_CHOICES, max_choices=3)
    reason = MultiSelectField(choices=REASON_CHOICES, max_choices=3)
    
    def __str__(self):
        return str(self.date) + " " + str(self.user)
    
    class Meta:
        ordering = ['date']

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