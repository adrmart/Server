from rest_framework import serializers

from django.contrib.auth.models import User, Group
from cronovisor.models import Street, Image, Marker

class ImageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'

class StreetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Street
		fields = '__all__'

class MarkerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marker
		fields = '__all__'
