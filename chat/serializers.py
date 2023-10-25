# serializers.py
from rest_framework import serializers
from .models import UserProfile, Room, Message , Members
from rest_framework.authtoken.models import Token

class UserProfileSerializer(serializers.ModelSerializer):
    
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ('id', 'username'   , 'public_key')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'text', 'sender', 'room', 'created_at')

class MemberSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    user = UserProfileSerializer()

    class Meta:
        Moel = Members
        field = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)
