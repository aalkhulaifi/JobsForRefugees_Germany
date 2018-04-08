from django.urls import path
from . import views

urlpatterns = [
    path('tasker/signup/', views.tasker_signup, name='taskersignup'),
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_logout, name='signout'),
]