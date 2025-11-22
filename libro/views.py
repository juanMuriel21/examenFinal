from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Mlibro
from .serializers import libroSerializer

class libroViewSet(viewsets.ModelViewSet):
    queryset = Mlibro.objects.all()
    serializer_class = libroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']  # Filtrado por autor

# Create your views here.
