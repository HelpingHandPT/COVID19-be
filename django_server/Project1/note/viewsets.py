from rest_framework import viewsets
from . import models
from . import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

class NotesViewSet(viewsets.ModelViewSet):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer