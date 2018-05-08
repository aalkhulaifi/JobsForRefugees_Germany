from django.urls import path
from api.views import CategoryListView, AreaListView, UserListView,TaskerListView,TaskRequestListView, AreaCreateView, UserCreateView, TaskRequestCreateView,UserProfileDetailView

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='list'),
    path('area/', AreaListView.as_view(), name='Area'),
    path('user/', UserListView.as_view(), name='User'),
    path('tasker/', TaskerListView.as_view(), name='Tasker'),
    path('task_Request/', TaskRequestCreateView.as_view(), name='Task_Request'),
    path('create_User/', UserCreateView.as_view(), name='create_User'),
    path('create_Area/', AreaCreateView.as_view(), name='create_Area'),
    path('create_Task_Request/', TaskRequestCreateView.as_view(), name='create_Task_Request'),
    path('detail/<int:user_id>/', UserProfileDetailView.as_view(), name='detail'),
]
