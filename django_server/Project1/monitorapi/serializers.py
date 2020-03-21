from rest_framework import serializers
from .models import Notes, Monitors


class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ('id', 'text')


class MonitorsSerializer(serializers.ModelSerializer):
    notes = NotesSerializer(many=True, read_only=True)

    class Meta:
        model = Monitors
        fields = ('id','fullName', 'email', 'notes')
        extra_kwargs = {
            'notes': {'required': False},
            'email': {'required': False}
        }