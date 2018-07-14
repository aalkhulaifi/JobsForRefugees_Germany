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
	user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
	tasker = models.ForeignKey(Tasker,on_delete=models.CASCADE ,null=True, blank=True)
	date = models.DateField(auto_now=False,auto_now_add=False)
	time = models.TimeField(auto_now=False,auto_now_add=False)
	contact_number = models.PositiveIntegerField(null=True, blank=True)
	description = models.TextField()
	TASK_CHOICES = (
		('Approved', 'Approved'),
		('Denied', 'Denied'),
		('Pending', 'Pending'),
	)
	status = models.CharField(max_length=20, choices=TASK_CHOICES, default='Pending')



class Notification(models.Model):
	# ForeignKey to the user model
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	tasker = models.ForeignKey(Tasker, on_delete=models.CASCADE,null=True)
	notification = models.ForeignKey(Task_Request, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return '{}'.format(self.user)

# # rating of the taskers by the users
# class Rating(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	rating = models.ForeignKey(Tasker, on_delete=models.CASCADE)
# 	def __str__(self):
# 		return self.user



class Billing(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	# the price should include the tasker rate in Tasker model
	price = models.ForeignKey(Tasker, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
