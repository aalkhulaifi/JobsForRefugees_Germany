from django.urls import path
from . import views

urlpatterns = [
	path('registration/', views.registration_path, name='registration'),
    path('tasker/signup/', views.tasker_signup, name='taskersignup'),
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_logout, name='signout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.user_edit_profile, name='edit_profile'),
    path('tasker_edit_profile/', views.tasker_edit_profile, name='tasker_edit_profile'),
    path('request/send/', views.making_a_request, name="request" ),
    path('send_a_request_to_a_tasker/<int:send_request_id>/', views.send_a_request_to_a_tasker, name="send_a_request_to_a_tasker"),
    path('task_list/', views.task_list, name="task" ),
]