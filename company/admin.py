from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Department)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('User', 'Department','Designation','JoiningDate','EmployeStatus')
    search_fields = ('Email',)
admin.site.register(UserProfile,UserProfileAdmin)

class Leave_ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('User', 'Name','LeaveType','HR_approval','PM_approval','MD_approval',"SubmitionDate")
    search_fields = ('Email',)
admin.site.register(Leave_Applications,Leave_ApplicationsAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('Titel',)
    search_fields = ('Titel',)
admin.site.register(Announcement,AnnouncementAdmin)

# parmitions
class permission_AddUserAdmin(admin.ModelAdmin):
    list_display = ('User','View','Edit')
    search_fields = ('User',)
admin.site.register(permission_AddUser,permission_AddUserAdmin)

class permission_UserListAdmin(admin.ModelAdmin):
    list_display = ('User','View','Edit')
    search_fields = ('User',)
admin.site.register(permission_UserList,permission_UserListAdmin)

class permission_LeaveApprovelAdmin(admin.ModelAdmin):
    list_display = ('User','View','Edit')
    search_fields = ('User',)
admin.site.register(permission_LeaveApprovel,permission_LeaveApprovelAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('Employee','Signing_In_Time','Prayer_Break','Dinner_Break','Tea_Break','Signing_Out_Time','Date')
    search_fields = ('Date', 'Employee')
admin.site.register(Attendance,AttendanceAdmin)