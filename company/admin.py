from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Announcement)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('User', 'Department','Designation','JoiningDate','EmployeStatus')
    search_fields = ('Email',)
admin.site.register(UserProfile,UserProfileAdmin)
