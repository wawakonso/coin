# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class TrackActivity(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    deceased = models.BooleanField(default=False)

    class Meta:
        abstract = True


# Create your models here.
