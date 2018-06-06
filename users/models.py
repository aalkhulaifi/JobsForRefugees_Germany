from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Category, Area
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.db.models.signals import post_save

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
	date = models.DateTimeField(default=timezone.now)
	time = models.DateTimeField(blank=True, null=True)
	contact_number = models.PositiveIntegerField(null=True, blank=True)
	description = models.TextField()
	TASK_CHOICES = (
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
        ('Pending', 'Pending'),
    )
	status = models.CharField(max_length=20, choices=TASK_CHOICES, default='Pending')
	
	def __str__(self):
		return '{}'.format(self.user)

	def get_absolute_url(self):
		return "request/%d/view" % self.pk

	def create_notification(sender, **kwargs):
		for key, value in kwargs.items():
			task_request = Notification.objects.create(user=kwargs['instance'])

	post_save.connect(create_notification, sender=User)


class Notification(models.Model):
	notification = models.ForeignKey(Task_Request, on_delete=models.CASCADE ,null=True, blank=True)
	message = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
	tasker = models.ForeignKey(Tasker,on_delete=models.CASCADE ,null=True, blank=True)
	time = models.DateTimeField(blank=True, null=True)
	mark_as_read = models.CharField(max_length=20)
	
	def __str__(self):
		return '{}'.format(self.user)
