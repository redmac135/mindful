from django.db import models
from django.contrib.auth.models import User

import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    last_sent_confirmation = models.DateTimeField(auto_now_add=True)

    def check_last_sent(self, current):
        checktime = self.last_sent_confirmation + datetime.timedelta(hours=2)
        if checktime > current:
            return checktime
        else:
            return True

    def send_activation_email(self, user, request):
        current_site = get_current_site(request)
        subject = 'Welcome to Mindful! Activate your Account'
        message = render_to_string('emails/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail(
            subject,
            message,
            'mindful.str@gmail.com',
            [user.email],
            fail_silently=False
        )

    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()