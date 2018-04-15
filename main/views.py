from .models import Category
from django.shortcuts import render
from django.utils import timezone

def home(request):
	context = {
		"category_list": Category.objects.all()
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html')

def category_list(request):
	today = timezone.now().date()
	context = {
		"object_list": Category.objects.all(),
		"today": today
	}
	return render(request, 'category_list.html', context)
