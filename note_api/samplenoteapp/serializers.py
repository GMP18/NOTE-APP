from rest_framework import serializers
from .models import noteapp

class NoteappSerializer(serializers.ModelSerializer):
	class Meta:
		model = noteapp
		fields = ('id', 'name', 'description')