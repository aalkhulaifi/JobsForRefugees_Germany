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

def category_detail(request, category_id):
	category = Category.objects.get(id=category_id)
	taskers = category.tasker_set.all()
	context = {
		"taskers": taskers
	}
	return render(request, 'category_detail.html', context)
