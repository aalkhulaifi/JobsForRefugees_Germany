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
    path('send_request/', views.make_a_request, name='request'),
    path('deniy/<int:request_id>', views.request_denied, name='deniy_request'),
    path('task_list/', views.task_list, name="task" ),
    path('notifications/', views.notifications, name='notifications'),

#     path('request_success/',views.request_success),
#     path('send_request/',views.send_request),
]