from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView ,TaskerCreateAPIView,TaskerLoginAPIView,Task_RequestAPIView,Task_RequestListView, Task_RequestDetailView,Task_RequestUpdateView 

urlpatterns = [
	path('signupapi/', UserCreateAPIView.as_view(), name='signupapi'),
	path('signinapi/', UserLoginAPIView.as_view(), name='signinapi'),
	path('taskersignin/', TaskerLoginAPIView.as_view(), name='taskersigninapi'),
	path('taskersignup/', TaskerCreateAPIView.as_view(), name='taskersignupapi'),
	path('api_task/', Task_RequestAPIView.as_view(), name='api_task'),
	path('list_api/', Task_RequestListView.as_view(), name='list_api'),
	path('detail/<int:object_id>/', Task_RequestDetailView.as_view(), name='apidetail'),
	path('update/<int:object_id>/', Task_RequestUpdateView.as_view(), name='apiupdate'),

]