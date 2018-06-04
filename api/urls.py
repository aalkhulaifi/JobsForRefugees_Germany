from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView

urlpatterns = [
	path('signup/', UserCreateAPIView.as_view(), name='signup'),
	path('signin/', UserLoginAPIView.as_view(), name='signin'),
]