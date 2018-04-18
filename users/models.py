from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Category, Area

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

class Profile(models.Model):
	general_handyman = models.ForeignKey(Tasker, on_delete=models.CASCADE)
	is_general_handyman = models.BooleanField(default=False)