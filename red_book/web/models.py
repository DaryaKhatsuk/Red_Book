from django.db import models


class RedBook (models.Model):
    id = models.IntegerField (primary_key=True)
    name = models.CharField(max_length=255)
    name_L = models.CharField(max_length=255)
    name_B = models.CharField(max_length=255)
    priority = models.CharField(max_length=200)
