from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, Http404
from .forms import Signup ,Login, TaskerSignup, TaskerEditProfileForm, UserEditProfileForm,Task_RequestForm
from django.contrib.auth import login , logout,authenticate
from .models import Tasker, User, Task_Request,Notification, Billing
from django.conf import settings
from django.contrib import messages
from main import views
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def registration_path(request):
	return render(request, 'register.html')

def user_signup(request):
	form = Signup()
	if request.method == 'POST':
		form = Signup(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.email

			user.set_password(user.password)
			user.save()

			login(request, user)
			return redirect("home")
	context = {
		"form":form,
	}
	return render(request, 'signup.html', context)

def user_signin(request):
	form = Login()
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():

			username = form.cleaned_data['email']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('home')
	context = {
		"form":form
	}
	return render(request, 'login.html', context)

def user_logout(request):
	logout(request)
	return redirect("signin")


def tasker_signup(request):
	form1 = Signup()
	form2 = TaskerSignup()
	if request.method == 'POST':
		form1 = Signup(request.POST)
		form2 = TaskerSignup(request.POST, request.FILES)
		if form1.is_valid() and form2.is_valid():
			user = form1.save(commit=False)
			user.username = user.email
			user.set_password(user.password)
			user.is_tasker = True
			user.save()
			tasker = form2.save(commit=False)
			tasker.user = user
			tasker.save()
			form2.save_m2m()
			login(request, user)
			return redirect("home")
		# print (form1.errors)
		# print (form2.errors)
	context = {
		"form1":form1,
		"form2":form2,
	}
	return render(request, 'taskersignup.html', context)

def user_profile(request):
	if request.user.is_anonymous:
		return redirect('signin')
	return render(request, 'user_profile.html')

def user_edit_profile(request):
	if request.user.is_tasker:
		raise Http404
	form = UserEditProfileForm(request.POST or None, instance=request.user)
	if form.is_valid():
		form.save()
		return redirect('profile')
	context = {
		"form":form,

	}
	return render(request, 'user_edit_profile.html', context)

def tasker_edit_profile(request):
	if not request.user.is_tasker:
		raise Http404
	if request.method == 'POST':
		form1 = UserEditProfileForm(request.POST or None,request.FILES, instance=request.user)
		form2 = TaskerEditProfileForm(request.POST or None,request.FILES, instance=request.user.tasker)
		if form1.is_valid() and form2.is_valid():
			form1.save()
			form2.save()
			return redirect('profile')
		else:
			messages.error(request, ('Please correct the error below.'))
	else:
		form1 = UserEditProfileForm(instance=request.user)
		form2 = TaskerEditProfileForm(instance=request.user.tasker)
	context = {
		"form1":form1,
		"form2":form2,

	}
	return render(request, 'tasker_edit_profile.html',context)


def create_request(request, tasker_id):
	if request.user.is_anonymous:
		return redirect('signin')
	# Is there a way to assign the current user as a sender(creator) of this request by default?
	tasker = Tasker.objects.get(id=tasker_id)

	# widegts for time and date!
	form = Task_RequestForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		task = form.save(commit=False)
		task.user=request.user
		task.tasker = tasker
		task.save()

		Notification.objects.create(user=tasker.user, notification=task)
		messages.success(request, "Successfully Created request at date %s at time %s!"%(task.date,task.time))

		return redirect("request_list")
	context = {
	"form": form,
	"tasker": tasker,
	}
	return render(request, 'request_form.html', context)

# list of requests (filtered by id) (tasks) for the tasker view
def request_list(request):
	if not request.user.is_tasker:
		return redirect("task_list")
# filter the request by the current tasker id (requests that had been sent to this particular tasker) 
	reqs = Task_Request.objects.filter(tasker=request.user.is_authenticated)
	paginator = Paginator(reqs, 5) # Show 5 requests per page

	page = request.GET.get('page')
	reqs = paginator.get_page(page)
	context={
	'request_list': reqs,
	}
	return render(request,'request_list.html',context)


def sent_task(request, pk):
	instance = Task_Request.objects.get(pk=pk)
	form = Task_RequestForm(request.GET or None, request.FILES or None)
	if form.is_valid():
		form = form.save(commit=False)
		form.save()
		return redirect("request_list")

	context = {
	"form":form,
	"instance": instance,

	}

	return render(request,'request.html', context)

#  tasker view request either accept(if accept request status = Approved) shows in tasks_list and request_list

def accepted_request(request, request_id):
	if not request.user.is_tasker:
		return redirect('task_list')
	request = Task_Request.objects.get(id = request_id)
	request.status = 'Approved'
	request.save()
	
# and the object(request item/card) shows in the user request list

	return redirect('request_list')

# if tasker deny request,status = Approved

def deni_request(request, request_id):
	if not request.user.is_tasker:
		return redirect('task_list')
	request = Task_Request.objects.get(id = request_id)
	request.status = 'Denied'
	request.save()

	return redirect('request_list')


# the user sent request list (filtered by id) show the status true if the user(tasker) accepted the request

def task_list(request):
	if request.user.is_tasker:
		return redirect('request_list')
# filter the request by the current user id
# doesn't show the whole list of objects, it only displays 3 pages and 15 objects in total
	reqs= Task_Request.objects.filter(user=request.user)
	paginator = Paginator(reqs, 5) # Show 5 requests per page
	page = request.GET.get('page')
	reqs = paginator.get_page(page)
	try:
		reqs = paginator.page(page)

	except PageNotAnInteger:
		reqs = paginator.page(1)
	except EmptyPage:
		reqs = paginator.page(paginator.num_pages)
		
	context={
	'request_list': reqs,
	
	}
	return render(request,'task_list.html',context)


def tasker_notification_list(request):
	reqs = Notification.objects.all()

	context={
	'request_list': reqs,
	
	}
	return render(request,'tasker_notifications.html',context)


# notification badge
def notification_badge(request, notification_id):
	notification = Task_Request.objects.get(id=notification_id)

	impressed, created = Notification.objects.get_or_create(tasker=request.user, notification=notification)
	if created:
		action="notification"
	else:
		action="notification_deleted"
		impressed.delete()

	notification_Notification_count = Notification.objects.filter(notification=notification).count()

	context = {
		"action":action,
		"count":notification_Notification_count
	}
	return JsonResponse(context, safe=False)

def billing_list(request):

	bill = Billing.objects.all()
	paginator = Paginator(bill, 5) # Show 5 requests per page

	page = request.GET.get('page')
	bill = paginator.get_page(page)
	context={
	'billing_list': bill,
	}
	return render(request,'bills_list.html',context)

# rating view 
