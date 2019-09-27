from rest_framework import serializers

from .models import User, UserAnswer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


class TopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
