from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, Http404
from .forms import Signup ,Login, TaskerSignup, TaskerEditProfileForm, UserEditProfileForm,Task_RequestForm
from django.contrib.auth import login , logout,authenticate
from .models import Tasker, User, Task_Request
from django.conf import settings
from django.contrib import messages
from django.template import RequestContext
from main import views
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

def notifications(request):
	return render(request, 'notifications.html')

def requests(request):
	if not request.user.is_authenticated:
		return redirect('signin')
	form = Task_RequestForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form = form.save(commit=False)
		form.save()
		return redirect("request_list")
	context = {
	"form": form,
	}
	return render(request, 'request_form.html', context)

def accept_request(request, request_id):
	if not request.user.is_tasker:
		raise Http404
	request = Task_Request.objects.get(id=request_id)
	request.save()

	return redirect("request")

def request_list(request):
	if not request.user.is_tasker:
		raise Http404
	reqs= Task_Request.objects.all()
	users = []
	for req in reqs:
		users.append(req.user)
	users = list(set(users))
	context={
	'request_list': users,
	}
	return render(request,'request_list.html',context)

def request(request, pk):
	if not request.user.is_tasker:
		raise Http404
	instance = Task_Request.objects.get(pk=pk)
	form = Task_RequestForm()

	if request.method=="GET":
		form = Task_RequestForm(request.GET)


	context = {
	"form":form,
	"instance": instance,

	}

	return render(request,'request.html', context)

def sent_request_list(request):
	if request.user.is_tasker:
		raise Http404
	reqs= Task_Request.objects.all()
	users = []
	for req in reqs:
		users.append(req.user)
	users = list(set(users))
	context={
	'request_list': users,
	}
	return render(request,'request_list.html',context)

