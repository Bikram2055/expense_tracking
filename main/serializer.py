from rest_framework import serializers
from .models import Record
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "id", "email"]

class RecordSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # user = serializers.SerializerMethodField()  # for get_user method
    class Meta:
        model = Record
        fields = ["id", "name", "user"]
        # depth = 1
        
        # def get_user(self, obj):
        #     user_instance = obj.user  # Assuming 'user' is the related field in the Record model
        #     return UserSerializer(user_instance).data