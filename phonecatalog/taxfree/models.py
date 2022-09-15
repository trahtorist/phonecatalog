from django.db import models


class Puesc(models.Model):
    taxid = models.CharField(max_length=255)
    puesc_answer = models.TextField(blank=True)
