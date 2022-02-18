from django.db import models

from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

ADJECTIVE_CHOICES = (
    (1, 'Happy'),
    (2, 'Confident'),
    (3, 'Excited'),
)

REASON_CHOICES = (
    (1, 'Family'),
    (2, 'Friends'),
    (3, 'Work'),
    (4, 'School'),
)

# Create your models here.
class ReflectionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    feeling = models.IntegerField()
    adjective = MultiSelectField(choices=ADJECTIVE_CHOICES, max_choices=3)
    reason = MultiSelectField(choices=REASON_CHOICES, max_choices=3)
    rose = models.CharField(max_length=500, blank=True)
    bud = models.CharField(max_length=500, blank=True)
    thorn = models.CharField(max_length=500, blank=True)
