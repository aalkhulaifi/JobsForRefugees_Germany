from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Category, Area
from django.utils import timezone

class User(AbstractUser):
	email = models.EmailField(unique=True)
	is_tasker = models.BooleanField(default=False)

class Tasker(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField(upload_to='tasker_profile_pics')
	profession = models.TextField()
	rate = models.DecimalField(max_digits=10, decimal_places=2)
	categories = models.ManyToManyField(Category)
	areas = models.ManyToManyField(Area)
	age = models.PositiveIntegerField(default=18)
	number = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return self.user.get_full_name()

class Task_Request(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user' ,null=True, blank=True)
	tasker = models.ForeignKey(Tasker,on_delete=models.CASCADE , related_name='recipient' ,null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	time = models.DateTimeField(blank=True, null=True)
	contact_number = models.PositiveIntegerField(null=True, blank=True)
	description = models.TextField()
	status = models.NullBooleanField(default=False)
	def __str__(self):
		return 'Request from: {}'.format(self.user)
		
	def get_absolute_url(self):
		return "request/%d/view" % self.pk
