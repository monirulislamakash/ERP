from django.contrib import admin
from django.urls import path
from . views import *
app_name = 'company'
urlpatterns = [
    path('', index,name="dashbord"),
    path('addUser', addUser,name="addUser"),
    path('UserList', UserList,name="UserList"),
    path('profile', Profile,name="profile"),
    path('userprofile/<str:email>', userProfile,name="userprofile"),
]