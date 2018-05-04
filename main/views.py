from .models import Category
from users.models import Tasker
from .forms import TaskerSearch
from django.shortcuts import render, redirect
from django.utils import timezone
from main.models import Area
from django.db.models import Q
from users.models import Tasker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	form = TaskerSearch()
	taskers = Tasker.objects.none()
	categories = request.GET.get('categories')
	areas = request.GET.get('areas')
	if categories and areas:
		taskers = Tasker.objects.filter(
			categories__id=categories,
			areas__id=areas
			)
	context = {
		"taskers": taskers,
		"categories": categories,
		"areas": areas,
		"form": form,
	}
	return render(request, 'home.html', context)

def list(request):
	form = TaskerSearch()
	taskers = Tasker.objects.none()
	categories = request.GET.get('categories')
	areas = request.GET.get('areas')
	if categories and areas:
		taskers = Tasker.objects.filter(
			categories__id=categories,
			areas__id=areas
			)
	paginator = Paginator(categories, 3) 
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)

	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
		
	context = {
		"taskers": taskers,
		"categories": categories,
		"areas": areas,
		"form": form,
		"categories": objects,

	}
	return render(request, 'list.html', context)

def about(request):
	return render(request, 'about.html')

def tasker_profile_detail(request, tasker_id):
	context = {
			"user": Tasker.objects.get(id=tasker_id)
		}
	return render(request, 'tasker_profile_detail.html', context)

def billing(request):
	return render(request, 'billing.html')

