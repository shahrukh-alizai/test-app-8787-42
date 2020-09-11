from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        blank=True,
        max_length=150,
    )
    news = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    phone = models.BigIntegerField(
        null=True,
        blank=True,
    )
    book = models.BigIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body3 = models.TextField(
        blank=True,
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
