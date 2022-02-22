from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(max_length=9)

    def __str__(self):
        return self.user

class RegistrationToken(models.Model):
    token = models.CharField(max_length=9)
    valid = models.BooleanField()

    def __str__(self):
        return self.token