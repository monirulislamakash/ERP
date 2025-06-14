from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def addUser(request):
    Departments=Department.objects.all()
    if request.method=="POST":
        getInput=request.POST.get
        getFiles=request.FILES
        try:
            user=User.objects.get(username=getInput('email'))
            return render(request,"addEmployee.html",{'addStatus':"error"})
        except User.DoesNotExist:
            user=User.objects.create_user(username=getInput('email'),password='R@yL0gin#P@$$w0rd@')
            Departments=Department.objects.get(Department=getInput('Department'),)
            SaveFrom=UserProfile(
                User=user,
                FirstName=getInput('firstname'),
                LastName=('lastname'),
                UserAccess=getInput('UserAccess'),
                Email=getInput('email'),
                Designation=getInput('Designation'),
                Department=Departments,
                PermanentAddress=getInput('PermanentAddress'),
                PresentAddress=getInput('PresentAddress'),
                PhoneNumbe=getInput('phonenumber'),
                EmergencyPhoneNumber=getInput('EmergencyPhoneNumber'),
                Salary=getInput('Salary'),
                JoiningDate=getInput('JoiningDate'),
                PermanencyDate=getInput('PermanencyDate'),
                Image=getFiles['Image'],
                BankName=getInput('BankName'),
                BankAccountName=getInput('BankAccountName'),
                BankAccountNumber=getInput('BankAccountNumber'),
                BankBranchName=getInput('BankBranchName'),
                BankSwiftCode=getInput('BankSwiftCode'),
                BankRoutingNumber=getInput('BankRoutingNumber'),
                BankPhoneNumber=getInput('BankPhoneNumber'),
                NIDNumber=getInput('NIDNumber'),
                TINNumber=getInput('TINNumber'),
                FatherName=getInput('FatherName'),
                MotherName=getInput('MotherName'),
                EmployeStatus=getInput('EmployeStatus'),
                AppointmentLetter=getFiles['AppointmentLetter'],
                NDA=getFiles['NDA'],
                SalaryIncrementLetter=getFiles['SalaryIncrementLetter'],
                PromotionLetter=getFiles['PromotionLetter'],
                )
            SaveFrom.save()
            return render(request,"addEmployee.html",{'addStatus':"success"})
    sendvar={
        'Departments':Departments,
    }
    return render(request,"addEmployee.html",sendvar)

def UserList(request):
    if request.method=="POST":
        Search=request.POST.get('Search')
        try:
            Designation=UserProfile.objects.filter(Designation__icontains=Search)
            firstName=UserProfile.objects.filter(FirstName__icontains=Search)
            getDepartments=Department.objects.get(Department=Search)
            Departments=UserProfile.objects.filter(Department=getDepartments)
            lastName=UserProfile.objects.filter(LastName__icontains=Search)
            phone=UserProfile.objects.filter(PhoneNumbe__icontains=Search)
            email=UserProfile.objects.filter(Email__icontains=Search)
            name=firstName.union(lastName)
            name_Designation=name.union(Designation)
            name_Designation_Department=name_Designation.union(Departments)
            name_Designation_Department_phone=name_Designation_Department.union(phone)
            name_Designation_Department_phone_email=name_Designation_Department_phone.union(email)
            senvar={
                'getAllUser':name_Designation_Department_phone_email,
            }
            return render(request,"employeeList.html",senvar)
        except Department.DoesNotExist:
            Designation=UserProfile.objects.filter(Designation__icontains=Search)
            firstName=UserProfile.objects.filter(FirstName__icontains=Search)
            lastName=UserProfile.objects.filter(LastName__icontains=Search)
            phone=UserProfile.objects.filter(PhoneNumbe__icontains=Search)
            email=UserProfile.objects.filter(Email__icontains=Search)
            name=firstName.union(lastName)
            name_Designation=name.union(Designation)
            name_Designation_phone=name_Designation.union(phone)
            name_Designation_phone_email=name_Designation_phone.union(email)
            senvar={
                'getAllUser':name_Designation_phone_email,
            }
            return render(request,"employeeList.html",senvar)
    getAllUser=UserProfile.objects.all()
    senvar={
        'getAllUser':getAllUser,
    }
    return render(request,"employeeList.html",senvar)

def Profile(request):
    getUser=User.objects.get(username=request.user)
    getMyInfo=UserProfile.objects.get(User=getUser)
    sendvar={
        'getMyInfo':getMyInfo,
    }
    print(getUser)
    print(request.user)
    return render(request,"profile.html",sendvar)

def userProfile(request,email):
    userMyInfo=UserProfile.objects.get(Email=email)
    sendvar={
        'userMyInfo':userMyInfo
    }
    return render(request,"userProfile.html",sendvar)