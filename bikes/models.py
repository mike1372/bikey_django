from django.db import models

class Bike(models.Model):
		name = models.CharField(max_length=100)
		bike_make = models.CharField(max_length=100)
		bike_model = models.CharField(max_length=100)
		bike_type = models.CharField(max_length=100)
		colour = models.CharField(max_length=100)
		wheel_diameter = models.FloatField()
		weight = models.FloatField()

		def __unicode__(self):	# Note still using Python v2.7 so using unicode instead of str
				return self.name

class Chainring(models.Model):
    bike = models.ForeignKey(Bike)
    size = models.IntegerField()

    def __int__(self): # This caused issues when trying to render on the admin page
    											 # "coercing to Unicode: need string or buffer, int found", changed to __int__
				return self.size

class CassetteSprocket(models.Model):
		bike = models.ForeignKey(Bike)
		size = models.IntegerField()

		def __int__(self):
				return self.size