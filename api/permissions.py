from rest_framework.generics import ListAPIView, CreateAPIView
from users.models import Tasker, User, Task_Request
from .serializers import Task_RequestCreateSerializer, UserCreateSerializer, TaskerCreateSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class Task_RequestListView(ListAPIView):
    queryset = Task_Request.objects.all()
    serializer_class = Task_RequestCreateSerializer
    permission_classes = [AllowAny]

class UserCreateSerializer(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated]

class TaskerCreateSerializer(CreateAPIView):
    serializer_class = TaskerCreateSerializer
    permission_classes = [IsAuthenticated]

class Task_RequestCreateSerializer(CreateAPIView):
    serializer_class = Task_RequestCreateSerializer
    permission_classes = [IsAuthenticated]

