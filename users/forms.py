from django import forms
from django.contrib.auth import get_user_model
from .models import Tasker, Task_Request, Notification
from django.forms.fields import DateField
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
import re
from datetimewidget.widgets import DateTimeWidget

from django.core.exceptions import ValidationError
User = get_user_model()

class GermanMobileField(forms.Field):
	def validate(self, value):
		if value != "":
			german_mobile = re.compile('^(4|9)(\d{12})$')
			german_mobile_match = german_mobile.match(value)
			if german_mobile_match == None:
				raise exceptions.ValidationError(_('Invalid Number: %(value)s'),
					code='invalid',
					params={'value': 'Please enter a German Mobile number'},
				)
			else:
				return value
		else:
			return value
	   

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