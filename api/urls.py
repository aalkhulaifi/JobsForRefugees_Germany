from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView ,TaskerCreateAPIView,TaskerLoginAPIView

urlpatterns = [
	path('signup/', UserCreateAPIView.as_view(), name='signup'),
	path('signin/', UserLoginAPIView.as_view(), name='signin'),
	path('taskersignin/', TaskerLoginAPIView.as_view(), name='taskersignin'),
	path('taskersignup/', TaskerCreateAPIView.as_view(), name='taskersignup'),
]