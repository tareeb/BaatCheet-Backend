from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
from channels.db import database_sync_to_async
from .models import  Message,  Members , Room
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['token']
        self.room_group_name = self.room_name 

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name

        )

     


        await self.accept()

    async def disconnect(self , clode_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data=None, bytes_data=None):
        text_data = json.loads(text_data)
        message = text_data['message']
        print(message)
        room = text_data['room']
        sender = text_data['sender']
        list_of_tokens =  await self.get_list(room , message )
        
        print(list_of_tokens)
        
        

                

        
        await self.channel_layer.group_send(
                list_of_tokens, {
                    'type' : 'chat_msg', # function to handle incomming msg
                    'chat' : message, # //message that will come.
                    'room_id' : room,
                    'sender' : sender
                }   

            )

    async def chat_msg(self , event):
        print(event)
        msg = event['chat']
        room_id = event['room_id']
        sender = event['sender']
        print(msg)

        await self.send(text_data=json.dumps({
                'text' : msg ,
                'sender' : sender ,
                'roomName' : room_id
        }))

    @database_sync_to_async
    def get_list(self, name , message):
        try:
            return_token = None
            members = Members.objects.filter(room__name=name)
            users = members.values_list('user', flat=True)
            tokens = Token.objects.filter(user__in=users)
            list_of_tokens = tokens.values_list('key', flat=True)
            room = Room.objects.get(name=name)
            sender = User.objects.get(auth_token__key=self.scope['url_route']['kwargs']['token'])
            
            mesaage = Message.objects.create(text = message , sender =sender , room = room )
            mesaage.save()
            for token in list_of_tokens:
                if token != self.scope['url_route']['kwargs']['token']:
                    return_token = token
            return return_token
            
        except Exception as e:
            print(e)
            
