from django.db import models
from users.models import Task_Request, Tasker,User
from django.utils import timezone

# Create your models here.
class Notification(models.Model):
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
