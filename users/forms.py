from django import forms
from django.contrib.auth import get_user_model
from .models import Tasker, Task_Request, Notification
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

class Signup(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name' ,'password']

		widgets={
		'password': forms.PasswordInput(),
		}

class Login(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())


class TaskerSignup(forms.ModelForm):
	class Meta:
		model = Tasker
		exclude = ['user', 'username']


class UserEditProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name' ,'username']

class TaskerEditProfileForm(forms.ModelForm):
	class Meta:
		model = Tasker
		exclude = ['user']

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class Task_RequestForm(forms.ModelForm):
	class Meta:
		model = Task_Request 
		fields = ['time', 'date', 'contact_number', 'description']
		widgets = {
			'date': DateInput(),
			'time': TimeInput(),
		}