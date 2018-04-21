from .models import Category
from users.models import Tasker
from django.shortcuts import render, redirect
from django.utils import timezone
from main.models import Area
from django.db.models import Q

def area_list(request):
	areas = Area.objects.all()
	# taskers = area.tasker.all()
	query = request.GET.get("q")
	if query:
		areas = areas.filter(
			name__icontains=query
			
			).distinct()

	context = {
		"areas": areas,
		# "tasker": tasker,

	}
	return render(request, 'area.html', context)
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
	return render(request, 'tasker_profile_detail.html', context)

def tasker_profile_detail(request, tasker_id):
	# tasker_profile = Category.objects.get(id=tasker_id)
	tasker = Tasker.objects.get(id=tasker_id)
	# profiles = tasker_profile.tasker_set.all()

	context = {
		# "profiles": profiles,
		"tasker": tasker,
	}
	return render(request, 'category_detail.html', context)

