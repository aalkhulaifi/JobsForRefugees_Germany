from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('list-view/', views.area_list, name='list-view'),
    path('category/taskers/<int:category_id>/', views.category_detail, name='category_detail'),
    path('main/category/taskers/profile/<int:tasker_id>/', views.tasker_profile_detail, name='tasker_profile_detail'),
]