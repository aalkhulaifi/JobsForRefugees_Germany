from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('list/', views.list, name='list'),
    path('billing/', views.billing, name='billing'),
    path('main/category/taskers/profile/<int:tasker_id>/', views.tasker_profile_detail, name='tasker_profile_detail'),
]