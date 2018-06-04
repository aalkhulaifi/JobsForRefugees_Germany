from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView ,TaskerCreateAPIView,TaskerLoginAPIView,Task_RequestAPIView,Task_RequestListView, Task_RequestDetailView,Task_RequestUpdateView 

urlpatterns = [
	path('signup/', UserCreateAPIView.as_view(), name='signup'),
	path('signin/', UserLoginAPIView.as_view(), name='signin'),
	path('taskersignin/', TaskerLoginAPIView.as_view(), name='taskersignin'),
	path('taskersignup/', TaskerCreateAPIView.as_view(), name='taskersignup'),
	path('task/', Task_RequestAPIView.as_view(), name='task'),
	path('list/', Task_RequestListView.as_view(), name='list'),
	path('detail/<int:object_id>/', Task_RequestDetailView.as_view(), name='detail'),
	path('update/<int:object_id>/', Task_RequestUpdateView.as_view(), name='update'),

]