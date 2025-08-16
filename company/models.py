from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
from tinymce import models as tinymce_models
# Create your models here.

class Department(models.Model):
    Department=models.CharField(max_length=50,default='NA')
    def __str__(self):
        return str(self.Department)
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

class Leave_Applications(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Subject=models.CharField(max_length=200, default="NA")
    Document=models.FileField(upload_to='media/user/LeaveApplication/', null=True)
    LeaveType=models.CharField(max_length=20,default="NA")
    SubmitionDate=models.DateField(max_length=50,default=datetime.today())
    FromDate=models.CharField(max_length=50,default="NA")
    ToDate=models.CharField(max_length=50,default="NA")
    Massage=models.TextField()
    HR_approval=models.BooleanField(default=False)
    PM_approval=models.BooleanField(default=False)
    MD_approval=models.BooleanField(default=False)
    HR_reject=models.BooleanField(default=False)
    PM_reject=models.BooleanField(default=False)
    MD_reject=models.BooleanField(default=False)
class Announcement(models.Model):
    Titel=models.CharField(max_length=300,default='')
    Announcement=tinymce_models.HTMLField()
    Post_Date=models.DateField(default=datetime.today())

class Attendance(models.Model):
    Employee=models.ForeignKey(User,on_delete=models.CASCADE)
    Signing_In_Time = models.CharField(default=0,max_length=20)
    Prayer_Break= models.CharField(default=0,max_length=20)
    Dinner_Break = models.CharField(default=0,max_length=20)
    Tea_Break = models.CharField(default=0,max_length=20)
    Signing_Out_Time = models.CharField(default=0,max_length=20)
    Date= models.DateField(default=datetime.today())

# ====================================================================================

class permission_AddUser(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    View=models.BooleanField(default=False)
    Edit=models.BooleanField(default=False)

class permission_UserList(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    View=models.BooleanField(default=False)
    Edit=models.BooleanField(default=False)
class permission_LeaveApprovel(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    View=models.BooleanField(default=False)
    Edit=models.BooleanField(default=False)
