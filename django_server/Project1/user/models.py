from django.db import models

# User Model
class Monitors(models.Model):
    userId = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    notes = models.ManyToManyField('Notes', related_name='monitors', blank=True)
    