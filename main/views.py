from .models import Category
from users.models import Tasker
from .forms import TaskerSearch
from django.shortcuts import render, redirect
from django.utils import timezone
from main.models import Area
from django.db.models import Q
from users.models import Tasker

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
	# # tasker_profile = Category.objects.get(id=tasker_id)
	taskers = Tasker.objects.get(id=tasker_id)
	# # profiles = tasker_profile.tasker_set.all()

	# context = {
	# 	# "profiles": profiles,
	# 	"tasker": tasker,
	# }
	taskers = Tasker.objects.none()
	areas = Area.objects.all()
		
	context = {
		"taskers": taskers,
		"areas": areas,
	}
	return render(request, 'category_detail.html', context)

