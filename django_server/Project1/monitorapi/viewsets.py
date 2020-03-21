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

class MonitorsViewSet(viewsets.ModelViewSet):
    queryset = models.Monitors.objects.all()
    serializer_class = serializers.MonitorsSerializer

    @action(detail=True, methods=['put'], name='Add Song')
    def add_notes(self, request, version, pk=None):
        notes_to_add = request.data['notes']
        queryset = models.Monitors.objects.all()
        monitor = get_object_or_404(queryset, pk=pk)
        for f in notes_to_add:
            monitor.notes.add(f)
        serializer = serializers.MonitorsSerializer(monitor)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], name='remove Song', url_path='remove_notes/(?P<note_id>[^/.]+)')
    def remove_notes(self, request, version, note_ud, pk=None):
        queryset = models.Monitors.objects.all()
        monitor = get_object_or_404(queryset, pk=pk)
        monitor.notes.remove(note_id)
        serializer = serializers.MonitorsSerializer(monitor)
        return Response(serializer.data)
