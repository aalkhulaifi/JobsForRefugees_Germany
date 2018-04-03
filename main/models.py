from django.db import models

# Create your models here.
class Category(models.Model):
	task_choices = (('General Handyman', 'General Handyman'), ('Moving and packing', 'Moving and packing'),('Home improvement', 'Home improvement'),('Mounting and installation', 'Mounting and installation'), ('Yard work', 'Yard work'),('Help moving', 'Help moving') )
# General Handyman ,Moving and packing , Furnniture assemby , Home improvement , Mounting and installation , Yard work , Help moving 
	task = models.CharField(('Task choices '), max_length=30, blank=False, choices=task_choices)
	

class Area(models.Model):
	name = models.CharField( max_length=255)
