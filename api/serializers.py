from rest_framework import serializers
from main.models import Category,Area
from users.models import User,Tasker,Task_Request

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class AreaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TaskerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasker
        fields = '__all__'


class TaskRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Request
        fields = '__all__'

class TaskRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Request
        fields = '__all__'
