from django.contrib import admin
from .models import Room, Message, Members, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Members)

