from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Members , Room , Message
from .serializers import UserProfileSerializer ,TokenSerializer , RoomSerializer , MessageSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from datetime import datetime, timedelta



@api_view(['POST'])
def login_view(request):
    # Get the username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')
    print(username , password)

    # Authenticate the user using the UserProfile model
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        

        # Get the user profile and serialize it
        token, created = Token.objects.get_or_create(user=user)
        _token = TokenSerializer(token)
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile)

        # Return the serialized user profile
        return Response({ 'token' : _token.data , 'user_profile':serializer.data } , status=status.HTTP_200_OK)

    # If the authentication failed, return an error response
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def signup_view(request):
    # Get the username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')

    # Create a new user object with the given username and password
    user = User.objects.create_user(username=username, password=password)

    # Create a new user profile object with the new user object
    user_profile = UserProfile.objects.create(user=user)
    token, created = Token.objects.get_or_create(user=user)
    _token = TokenSerializer(token)

    # Serialize the user profile object and return it in the response
    serializer = UserProfileSerializer(user_profile)
    
    return Response({'user data' : serializer.data , 'user_token' : _token.data},  status=status.HTTP_201_CREATED)

api_view(['GET'])
@authentication_classes([SessionAuthentication , TokenAuthentication])
@permission_classes([IsAuthenticated])
def lougout_view(request):
    logout(request)
    token = Token.objects.get(user=request.user)
    token.delete()
    
    return Response({'details' : 'user lougout'})



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request):

    user = request.user

    member_of = Members.objects.filter(user=user)
    if not member_of:
        return Response({'details' : 'you are not member of any room'})
    
    rooms = [member.room for member in member_of]
    serializer = RoomSerializer(rooms , many=True)
    return Response({'rooms' : serializer.data})


@api_view(['GET'])
@authentication_classes([SessionAuthentication , TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_room(request):
    name = request.GET.get('name')
    user = request.user
    try:
        room = Room.objects.get(name=name)
    except:
        room = None
    if room is None:

        room = Room.objects.create( owner = user, name=name)
        room.save()

        member = Members.objects.create(room=room)
        member.user.add(user)
        return Response({'details' : 'room created'})

    else:
            member, created = Members.objects.get_or_create(room=room)
            member.user.add(user)
            room = Room.objects.get(name=name)

            messages = Message.objects.filter(room = room)
            other_member = member.user.exclude(id=user.id).first()
           
            my_user = UserProfile.objects.get(user=other_member)
            user_serializer = UserProfileSerializer(my_user)

            
            if not messages:
                return Response({'user' : user_serializer.data , 'messages' : []})
            serializer = MessageSerializer(messages , many = True)

            
            
            return Response({'messages' : serializer.data , 'user' : user_serializer.data})


@api_view(['POST'])
@authentication_classes([SessionAuthentication , TokenAuthentication])
@permission_classes([IsAuthenticated])
def set_keys(request):
    user = request.user
    p_key = request.data.get('p_key')
    try:
        user_profile = UserProfile.objects.get(user=user)
    except:
        return Response({'details' : 'user not found'})
    user_profile.public_key = p_key
    print(user_profile.public_key)
    user_profile.save()
    return Response({'details' : 'ok'})

    

# @api_view(['GET'])
# def get_token_list(request , name):
#         members = Members.objects.filter(room__name=name)
#         users = members.values_list('user', flat=True)
#         tokens = Token.objects.filter(user__in=users)
#         serializer = TokenSerializer(tokens , many=True)
#         return Response({'tokens' : serializer.data})



# @api_view(['GET'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def join_room(request , name):
#     room = Room.objects.get(name=name)
#     user = request.user
#     member = Members.objects.create(user=user , room=room)
#     now = datetime.now()
#     one_hour_ago = now - timedelta(hours=1)
#     messages = Message.objects.filter(room = room , created_at__gte=one_hour_ago)
#     if not messages:
#         return Response({})
#     serializer = MessageSerializer(messages)
#     return Response({'messages' : serializer.data})









