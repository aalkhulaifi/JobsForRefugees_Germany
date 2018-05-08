from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView
from main.models import Category,Area
from users.models import User,Tasker,Task_Request
from api.serializers import CategoryListSerializer , AreaListSerializer,UserListSerializer,TaskerListSerializer, TaskRequestListSerializer , AreaCreateSerializer, UserCreateSerializer , TaskRequestCreateSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class AreaListView(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaListSerializer

class AreaCreateView(CreateAPIView):
    serializer_class = AreaCreateSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserProfileDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'

class TaskerListView(ListAPIView):
    queryset = Tasker.objects.all()
    serializer_class = TaskerListSerializer

class TaskRequestListView(ListAPIView):
    queryset = Task_Request.objects.all()
    serializer_class = TaskRequestListSerializer

class TaskRequestCreateView(CreateAPIView):
    serializer_class = TaskRequestCreateSerializer
