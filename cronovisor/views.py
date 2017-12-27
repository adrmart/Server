from django.shortcuts import render
from rest_framework import generics, viewsets
from cronovisor.models import Street, Image, Marker
from cronovisor.serializers import MarkerSerializer, StreetSerializer, ImageSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MarkerViewSet(viewsets.ModelViewSet):
	queryset = Marker.objects.all()
	serializer_class = MarkerSerializer
	permission_classes = (IsAuthenticated,)

class ImageViewSet(viewsets.ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer
	permission_classes = (IsAuthenticated,)

class StreetViewSet(viewsets.ModelViewSet):
	queryset = Street.objects.all()
	serializer_class = StreetSerializer
	permission_classes = (IsAuthenticated,)


