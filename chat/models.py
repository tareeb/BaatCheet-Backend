from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , unique=True)
    public_key = models.CharField(max_length=255 , null=True , blank=True)
    
    def __str__(self):
        return self.user.username

class Room(models.Model):
    name = models.CharField(max_length=255 , unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   
   

class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Members(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)


