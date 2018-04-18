from .models import Category
from users.models import Tasker
from django.shortcuts import render, redirect
from django.utils import timezone

def home(request):
	context = {
		"category_list": Category.objects.all(),
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')
