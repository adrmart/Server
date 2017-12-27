from django.db import models

# Create your models here.
class Street(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	represent = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Marker(models.Model):
	latitud = models.FloatField()
	longitud = models.FloatField()
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=100, null=True)
	
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

def upload_to(instance, filename):
	return 'media/{}/{}'.format(instance.id, filename)

class Image(models.Model):
	id_street = models.ForeignKey(Street, on_delete=models.CASCADE)
	id_marker = models.ForeignKey(Marker, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	description = models.TextField(null=True)
	image = models.ImageField(null=True, upload_to=upload_to)
	year = models.IntegerField()
	autor = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title
