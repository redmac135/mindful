from django.contrib import admin
from .models import ReflectionEntry, AdjectiveChoice, DailyQuote

# Register your models here.
admin.site.register(ReflectionEntry)
admin.site.register(AdjectiveChoice)
admin.site.register(DailyQuote)