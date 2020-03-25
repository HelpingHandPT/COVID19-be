from django.db import models
import uuid

# Notes Model
class Notes(models.Model):
    noteId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #authorId = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True)
    creationDate = models.DateTimeField() ,
    lastUpdate = models.DateTimeField() ,
    title = models.CharField(max_length=30, null=True)
    content = models.CharField(max_length=400, null=True)
    
    LOG = 'log'
    NOTE_TYPE = (
        ('healthLog', 'healthLog'),
        ('log', 'log'),
        ('user', 'user')
    )
    noteType = models.CharField(
        max_length=10,
        choices=NOTE_TYPE,
        default=LOG,
    )
    