from django.contrib import admin
from django.urls import path
from . views import *
app_name = 'company'
urlpatterns = [
    path('', index,name="dashbord"),
    path('addUser', addUser,name="addUser"),
    path('UserList', UserList,name="UserList"),
    path('profile', Profile,name="profile"),
    path('updatepassword', updatepassword,name="updatepassword"),
    path('attendance', attendance,name="attendance"),
    path('attendance/view',attendance,name="attendance"),
    path('userprofile/<str:email>', userProfile,name="userprofile"),
    path('UpdateProfile', UpdateProfile,name="UpdateProfile"),
    path('LeaveApplication', LeaveApplication,name="LeaveApplication"),
    path('LeaveApprovel', LeaveApprovel,name="LeaveApprovel"),
    path('LeaveApprovel/view/<int:id>', LeaveApprovelView,name="LeaveApprovelView"),
    path('LeaveApproveAction', LeaveApproveAction, name="LeaveApproveAction"),
    path('Announcements', announcements,name="Announcements"),
    path('department', department,name="department"),
    path('giveAccess', giveAccess,name="giveAccess"),
    path('login', login,name="login"),
    path('logout', logout,name="logout"),
]