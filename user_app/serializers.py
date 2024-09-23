# user_app/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from common.models import CustomGroup
from profile_app.models import UserDetails

class CustomGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomGroup
        fields = ['id', 'name']

class UserDetailsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() 
    groups = CustomGroupSerializer(source='user.groups', many=True, read_only=True)  # Fetch groups

    class Meta:
        model = UserDetails
        fields = '__all__'
