# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class OwnerProfile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    store_address = models.CharField(max_length=255)
    store_type = models.CharField(max_length=255)
    store_geocoordinates = models.CharField(max_length=255)
    store_id = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255)
    google_rating = models.FloatField()

    