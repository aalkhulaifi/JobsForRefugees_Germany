from .models import Category
from django.shortcuts import render
from django.utils import timezone

def home(request):
	return render(request, 'home.html')

def category_list(request):
	today = timezone.now().date()
	context = {
		"object_list": Category.objects.all(),
		"today": today
	}
	return render(request, 'category_list.html', context)
