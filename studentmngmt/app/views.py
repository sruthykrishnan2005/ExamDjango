from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class studentview(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=std
