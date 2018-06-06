from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tasker,Task_Request, Notification

admin.site.register(User, UserAdmin)
admin.site.register(Tasker)
admin.site.register(Task_Request)
admin.site.register(Notification)