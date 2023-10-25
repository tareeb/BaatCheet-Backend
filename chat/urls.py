from . import views
from django.urls import path

urlpatterns = [
       path('', views.login_view, name='login'),
       path('signup/', views.signup_view, name='signup'),
       path('home/', views.home, name='home'),
       path('logout/', views.lougout_view, name='logout'),
       path('create_room/', views.create_room, name='create_room'),
       path('set_key/', views.set_keys, name='set_key'),
]