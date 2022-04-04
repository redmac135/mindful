from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DefaultQuestion(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.time.strftime("%y-%m-%d %H:%M") + " " +  str(self.email)