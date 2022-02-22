from django.contrib import admin
from .models import Profile, RegistrationToken

# Register your models here.
admin.site.register(Profile)
admin.site.register(RegistrationToken)