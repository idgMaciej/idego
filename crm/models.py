from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)
    add_date = models.DateTimeField("date_add", default=timezone.now())

    def add_company(self):
        self.save()

    def __str__(self):
        return self.name
