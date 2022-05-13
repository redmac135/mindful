from django.db import models

# Create your models here.


class Resource(models.Model):
    class ResourceType(models.TextChoices):
        HOTLINES = "HTL", "Hotlines"
        COUNSELLING = "CNS", "Counselling"
        CBT = "CBT", "CBT Courses"

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    link = models.URLField(max_length=300)
    resource_t = models.CharField(max_length=3, choices=ResourceType.choices)

    def __str__(self):
        return self.name
