from noticeboard.models import *
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['id', 'description', 'username','created_at','updated_at']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']