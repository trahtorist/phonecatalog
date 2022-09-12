from django.db import models


class PhoneCatalog(models.Model):
    manufacturer = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    device_model = models.CharField(max_length=255)
    active = models.BooleanField()
