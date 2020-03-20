from django.db import models

# Notes Model
class Notes(models.Model):
    text = models.CharField(max_length=255, null=False)
    
# Monitor Model
class Monitors(models.Model):
    fullName = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    notes = models.ManyToManyField('Notes', related_name='monitors', blank=True)
    