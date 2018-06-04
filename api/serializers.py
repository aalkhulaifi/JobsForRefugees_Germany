from users.models import User, Tasker, Task_Request
from main.models import Category, Area
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.utils import timezone

# User signup and signin
class UserCreateSerializer(serializers.ModelSerializer):
	# To hash the password, the password is set the write_only attribute to True so it doesn't show in the JSON response
	password = serializers.CharField(write_only=True) 

	class Meta:
		model = User
		fields = ['email', 'password', 'is_tasker']
#  create method, so when the user object is create, the user passowrd will be hashed
		def create(self, validated_data):
			email = validated_data['email']
			password = validated_data['password']
			is_tasker = validated_data['is_tasker']
			new_user = User(email=email)
			new_user = User(is_tasker=is_tasker)
			new_user.set_password(password)
			new_user.save()
			return validated_data

class UserLoginSerializer(serializers.Serializer):
	email = serializers.CharField()
	password = serializers.CharField(write_only=True)  
	 # allow_blank = true, so that the user whose not logged in won't be able to geta token
	#  the read_only is true, beacuse if the user can write then the user should be able to create their own token
	token = serializers.CharField(allow_blank=True, read_only=True)


	def validate(self, data):
		email = data.get('email')
		password = data.get('password')

		try:
			user_obj = User.objects.get(email=email)
		except:
			raise serializers.ValidationError("This email does not exist")
			# chech_password method to check if the email and password combination is correct
		if not user_obj.check_password(password):
			raise serializers.ValidationError("Incorrect email/password combination!")
		
		# jwt_payload_handler variable takes the payload after it's created and assgin it to the user object to create the token
		# the jwt_encode_handler variable takes the payload an encode it
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		# after then payload is encrypted(toke), the token get included in the response 
		# by including it in the data dictionary
		data["token"] = token
		return data

# tasker signup and signin

class TaskerCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True) 

	class Meta:
		model = Tasker
		fields = ['user', 'profile_picture', 'profession', 'rate', 'categories', 'areas', 'age', 'number']

		def create(self, validated_data):
			user = validated_data['user']
			password = validated_data['password']
			new_user = User(user=user)
			new_user.set_password(password)
			new_user.save()
			return validated_data

class TaskerLoginSerializer(serializers.Serializer):
	user = serializers.CharField()
	password = serializers.CharField(write_only=True)  
	token = serializers.CharField(allow_blank=True, read_only=True)


	def validate(self, data):
		user = data.get('user')
		password = data.get('password')

		try:
			user_obj = User.objects.get(user=user)
		except:
			raise serializers.ValidationError("This user does not exist")
		if not user_obj.check_password(password):
			raise serializers.ValidationError("Incorrect user/password combination!")
		
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		data["token"] = token
		return data

# Request serializer
class Task_RequestCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task_Request
		fields = '__all__'
