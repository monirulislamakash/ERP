from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
# Create your models here.

class Department(models.Model):
    Department=models.CharField(max_length=50,default='NA')
    def __str__(self):
        return str(self.Department)

class Announcement(models.Model):
    AnnouncementTitel=models.CharField(max_length=200,default='NA')
    Announcement=models.TextField()
    def __str__(self):
        return str(self.AnnouncementTitel)

class UserProfile(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    UserAccess_CHOICES = (
    ('Employe', 'Employe'),
    ('Admin','Admin'),
    ('HR', 'HR'),
    ('Accounts', 'Accounts'),
    ('Project Manager', 'Project Manager'),
    )
    UserAccess=models.CharField(max_length=20, choices=UserAccess_CHOICES, default='Employe')
    FirstName=models.CharField(max_length=20,default='NA')
    LastName=models.CharField(max_length=20,default='NA')
    Email=models.CharField(max_length=100,default='NA')
    Designation=models.CharField(max_length=50,default='NA')
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    PermanentAddress=models.CharField(max_length=200,default='NA')
    PresentAddress=models.CharField(max_length=200,default='NA')
    PhoneNumbe=models.CharField(max_length=50,default='NA')
    EmergencyPhoneNumber=models.CharField(max_length=50,default='NA')
    Salary=models.CharField(max_length=20,default='NA')
    JoiningDate=models.CharField(max_length=50,default='NA')
    PermanencyDate=models.CharField(max_length=50,default='NA')
    Image=models.ImageField(upload_to='media/user/profile/', default="static/user/avater.webp")
    # Bank Details
    BankName=models.CharField(max_length=100,default='NA')
    BankAccountName=models.CharField(max_length=100,default='NA')
    BankAccountNumber=models.CharField(max_length=100,default='NA')
    BankBranchName=models.CharField(max_length=100,default='NA')
    BankSwiftCode=models.CharField(max_length=100,default='NA')
    BankRoutingNumber=models.CharField(max_length=100,default='NA')
    BankPhoneNumber=models.CharField(max_length=100,default='NA')
    # Bank Details End
    NIDNumber=models.CharField(max_length=20,default='NA')
    TINNumber=models.CharField(max_length=20,default='NA')
    FatherName=models.CharField(max_length=20,default='NA')
    MotherName=models.CharField(max_length=20,default='NA')
    EmployeStatus_CHOICES = (
    ('Probation','Probation'),
    ('Permanent', 'Permanent'),
    )
    EmployeStatus=models.CharField(max_length=20, choices=EmployeStatus_CHOICES, default='Probation')
    # Legal documents
    AppointmentLetter=models.FileField(upload_to='media/user/AppointmentLetter/',null=True)
    NDA=models.FileField(upload_to='media/user/NDA/',null=True)
    SalaryIncrementLetter=models.FileField(upload_to='media/user/NDA/',null=True)
    PromotionLetter=models.FileField(upload_to='media/user/PromotionLetter/',null=True)
    UserStatus=models.BooleanField(default=True)
    # Legal documents end
