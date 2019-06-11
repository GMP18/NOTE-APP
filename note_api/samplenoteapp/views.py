from django.shortcuts import render
from rest_framework import viewsets
from .models import noteapp
from .serializers import NoteappSerializer
# Create your views here.

class NoteappView(viewsets.ModelViewSet):
	queryset = noteapp.objects.all()
	serializer_class = NoteappSerializer