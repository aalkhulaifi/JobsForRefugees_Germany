from django import forms
from django.contrib.auth import get_user_model
from .models import Tasker, Task_Request
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

class Task_RequestForm(forms.ModelForm):
    class Meta:
        model = Task_Request 
        fields = ['tasker','time', 'date', 'contact_number', 'description']

    
