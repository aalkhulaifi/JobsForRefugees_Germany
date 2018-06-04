from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Notification
from main import views

# # Create your views here.
# def sent_task(request, pk):
# 	instance = Task_Request.objects.get(pk=pk)
# 	form = Task_RequestForm(request.GET or None, request.FILES or None)
# 	if form.is_valid():
# 		form = form.save(commit=False)
# 		form.save()
# 		return redirect("request_list")

# 	context = {
# 	"form":form,
# 	"instance": instance,

# 	}

# 	return render(request,'request.html', context)

# #  tasker view request either accept(if accept request status = Approved) shows in tasks_list and request_list

# def accepted_request(request, request_id):
# 	if not request.user.is_tasker:
# 		return redirect('task_list')
# 	request = Task_Request.objects.get(id = request_id)
# 	request.status = 'Approved'
# 	request.save()
	
# # and the object(request item/card) shows in the user request list

# 	return redirect('request_list')

# # if tasker deny request,status = Approved

# def deni_request(request, request_id):
# 	if not request.user.is_tasker:
# 		return redirect('task_list')
# 	request = Task_Request.objects.get(id = request_id)
# 	request.status = 'Denied'
# 	request.save()

# 	return redirect('request_list')
