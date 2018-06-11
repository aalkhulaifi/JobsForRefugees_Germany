from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import Notification

@receiver(pre_save, sender=Notification)
def auto_create_notification(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        tasker = user.tasker            
        Notification.objects.create(tasker=tasker,
                                    user=user,
                                    type="task_created")