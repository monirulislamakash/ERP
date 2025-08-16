from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
now = datetime.now()
# Create your views here.


@login_required(login_url='company:login')
def index(request):
    getUser=User.objects.get(username=request.user)
    getMyInfo=UserProfile.objects.get(User=getUser)
    sendvar={
        'users':getMyInfo
    }
    return render(request,"index.html",sendvar)

@login_required(login_url='company:login')
def addUser(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if user.UserAccess == "HR" or  user.UserAccess == "Project Manager" or  user.UserAccess == "Admin":
        Departments=Department.objects.all()
        if request.method=="POST":
            getInput=request.POST.get
            getFiles=request.FILES
            try:
                user=User.objects.get(username=getInput('email'))
                return render(request,"addEmployee.html",{'addStatus':"error",'users':user})
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
                return render(request,"addEmployee.html",{'addStatus':"success",'users':user})
        sendvar={
            'Departments':Departments,
            'users':user
        }
        return render(request,"addEmployee.html",sendvar)
    return redirect('company:dashbord')

@login_required(login_url='company:login')
def UserList(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if user.UserAccess == "HR" or  user.UserAccess == "Project Manager" or  user.UserAccess == "Admin":
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
                    'users':user
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
                    'users':user
                }
                return render(request,"employeeList.html",senvar)
        getAllUser=UserProfile.objects.all()
        senvar={
            'getAllUser':getAllUser,
            'users':user
        }
        return render(request,"employeeList.html",senvar)
    return redirect('company:dashbord')

@login_required(login_url='company:login')
def Profile(request):
    getUser=User.objects.get(username=request.user)
    getMyInfo=UserProfile.objects.get(User=getUser)
    LeaveApplication=Leave_Applications.objects.all().order_by('-id')
    sendvar={
        'getMyInfo':getMyInfo,
        'LeaveApplication':LeaveApplication,
        'users':getMyInfo
    }
    return render(request,"profile.html",sendvar)

@login_required(login_url='company:login')
def updatepassword(request):
    getUser=User.objects.get(username=request.user)
    getMyInfo=UserProfile.objects.get(User=getUser)
    LeaveApplication=Leave_Applications.objects.all().order_by('-id')
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        if not check_password(old_password, request.user.password):
            sendvar={
                'error':"Your old password was entered incorrectly. Please try again.",
                'getMyInfo':getMyInfo,
                'LeaveApplication':LeaveApplication,
                'users':getMyInfo
            }
            return render(request, 'profile.html',sendvar)

        if new_password1 != new_password2:
            sendvar={
                'error':"The two new password fields didn't match..",
                'getMyInfo':getMyInfo,
                'LeaveApplication':LeaveApplication,
                'users':getMyInfo
                
            }
            return render(request, 'profile.html',sendvar)

        if len(new_password1) < 8:
            sendvar={
                'error':"New password must be at least 8 characters long.",
                'getMyInfo':getMyInfo,
                'LeaveApplication':LeaveApplication,
                'users':getMyInfo
            }
            return render(request, 'profile.html',sendvar)
        request.user.set_password(new_password1)
        request.user.save()
        update_session_auth_hash(request, request.user)
        sendvar={
            'success':"Your password was successfully updated!",
            'getMyInfo':getMyInfo,
            'LeaveApplication':LeaveApplication,
            'users':getMyInfo
            }
        return render(request, 'profile.html',sendvar)
    sendvar={
        'getMyInfo':getMyInfo,
        'LeaveApplication':LeaveApplication,
        'users':getMyInfo
    }
    return render(request,"profile.html",sendvar)


@login_required(login_url='company:login')
def UpdateProfile(request):
    getUser=User.objects.get(username=request.user)
    getMyInfo=UserProfile.objects.get(User=getUser)
    if request.method == "POST":
        getInput=request.POST.get
        print(getInput)
        getFiles=request.FILES
        if bool(getFiles)==True:
            pass
        getMyInfo.FirstName=getInput('firstname')
        getMyInfo.LastName=getInput('lastname')
        getMyInfo.Email=getInput('email')
        getMyInfo.PermanentAddress=getInput('PermanentAddress')
        getMyInfo.PresentAddress=getInput('PresentAddress')
        getMyInfo.PhoneNumbe=getInput('phonenumber')
        getMyInfo.EmergencyPhoneNumber=getInput('EmergencyPhoneNumber')
        getMyInfo.BankName=getInput('BankName')
        getMyInfo.BankAccountName=getInput('BankAccountName')
        getMyInfo.BankAccountNumber=getInput('BankAccountNumber')
        getMyInfo.BankBranchName=getInput('BankBranchName')
        getMyInfo.BankSwiftCode=getInput('BankSwiftCode')
        getMyInfo.BankRoutingNumber=getInput('BankRoutingNumber')
        getMyInfo.BankPhoneNumber=getInput('BankPhoneNumber')
        getMyInfo.NIDNumber=getInput('NIDNumber')
        getMyInfo.TINNumber=getInput('TINNumber')
        getMyInfo.FatherName=getInput('FatherName')
        getMyInfo.MotherName=getInput('MotherName')
        getMyInfo.save()
    sendvar={
        "getMyInfo":getMyInfo,
        'users':getMyInfo
    }
    return render(request,"UpdateProfile.html",sendvar)

@login_required(login_url='company:login')
def userProfile(request,email):
    userMyInfo=UserProfile.objects.get(Email=email)
    sendvar={
        'userMyInfo':userMyInfo,
        'users':userMyInfo
    }
    return render(request,"userProfile.html",sendvar)

@login_required(login_url='company:login')
def LeaveApplication(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if request.method=="POST":
        try:
            userinput=request.POST.get
            getUser=User.objects.get(username=request.user)
            user=UserProfile.objects.get(User=getUser)
            print(userinput("From"),userinput("To"))
            saveFrom=Leave_Applications(
                User=getUser,
                Name=user.FirstName +" "+ user.LastName,
                Subject=userinput('Subject'),
                LeaveType=userinput("LeaveType"),
                FromDate=userinput("From"),
                ToDate=userinput("To"),
                Massage=userinput('Massage')
            )
            if userinput("LeaveType") != "Selected Leave":
                saveFrom.save()
                sendvar={
                    "succes":"Your Application has been submitted successfully",
                    'users':user
                }
            return render(request,"LeaveApplicationForm.html",sendvar)
        except:
            sendvar={
                "error":"Something went wrong. Please try again.",
                'users':user
            }
            return render(request,"LeaveApplicationForm.html",sendvar)
    return render(request,"LeaveApplicationForm.html")

@login_required(login_url='company:login')
def LeaveApprovel(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if user.UserAccess == "HR" or  user.UserAccess == "Project Manager" or  user.UserAccess == "Admin":
        # Load all UserProfiles (without filtering by any specific field)
        user_profiles = UserProfile.objects.all()

        # Create a lookup: User.id → UserProfile
        profile_map = {profile.User_id: profile for profile in user_profiles}

        # Load all leave applications and join their related Users
        getAllApplications = Leave_Applications.objects.select_related('User').all()

        # Match applications to profiles using the map
        applications_with_profiles = [
            (application, profile_map.get(application.User_id)) for application in getAllApplications
        ]
        
        sendvar={
            'applications_with_profiles': applications_with_profiles,
            'userStatus':user,
            'users':user
        }
        return render(request, "LeaveApprovel.html", sendvar)
    else:
        return redirect('company:dashbord')


@login_required(login_url='company:login')
def LeaveApproveAction(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if request.method=="POST":
        getValue=request.POST.get('AR')
        getID=request.POST.get('id')
        if user.UserAccess == "HR":
            if getValue=="approved":
                aprov=Leave_Applications.objects.get(id=getID)
                aprov.HR_approval=True
                aprov.save()
            if getValue=="reject":
                aprov=Leave_Applications.objects.get(id=getID)
                aprov.HR_reject=True
                aprov.save()
        elif user.UserAccess == "Project Manager":
            if getValue=="approved":
                aprov=Leave_Applications.objects.get(id=getID)
                aprov.PM_approval=True
                aprov.save()
            if getValue=="reject":
                aprov=Leave_Applications.objects.get(id=getID)
                aprov.PM_approval=True
                aprov.save()
        elif user.UserAccess == "Admin":
            if getValue=="approved":
                aprov=Leave_Applications.objects.get(id=getID)
                aprov.MD_approval=True
                aprov.save()
            if getValue=="reject":
                aprov=Leave_Applications.objects.get(id=getID)
                aprov.MD_reject=True
                aprov.save()
    return redirect('company:LeaveApprovel')

@login_required(login_url='company:login')
def LeaveApprovelView(request,id):
    applications=Leave_Applications.objects.get(id=id)
    ApplyedUser=UserProfile.objects.get(User=applications.User)
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if user.UserAccess == "HR" or  user.UserAccess == "Project Manager" or  user.UserAccess == "Admin":
        sendvar={
            "ApplyedUser":ApplyedUser,
            "applications":applications,
            'user':user
        }
        return render(request, "LeaveDetails.html", sendvar)
    else:
        return redirect('company:dashbord')

@login_required(login_url='company:login')
def giveAccess(request):
    if request.method=="POST":
        pass
    return render(request,'giveAccess.html')

@login_required(login_url='company:login')
def announcements(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    if request.method=="POST":
        get_search=request.POST.get('SearchHear')
        get_announcements=Announcement.objects.filter(Titel__icontains=get_search)
        get_date=Announcement.objects.filter(Post_Date__icontains=get_search)
        appstor=get_announcements.union(get_date)
        sendvar={
        'announcements':appstor,
        'search':'search',
        'users':user
        }
        return render(request,'announcements.html',sendvar)
    get_announcements=Announcement.objects.last()
    sendvar={
        'announcements':get_announcements,
        'users':user
    }
    return render(request,'announcements.html',sendvar)
@login_required(login_url='company:login')
def attendance(request):
    if request.method=="POST":
        getresponse=request.POST.get
        getUser=User.objects.get(username=request.user)
        try:
            userCheck=Attendance.objects.get(Employee=request.user,Date=datetime.today())
            if userCheck.Signing_In_Time == "0":
                userCheck
            if userCheck.Prayer_Break == "0" and userCheck.Signing_In_Time != "0":
                userCheck.Prayer_Break=now.strftime("%H:%M:%S")
                userCheck.save()
            if userCheck.Dinner_Break == "0" and userCheck.Prayer_Break != "0":
                pass
            if userCheck.Tea_Break == "0" and userCheck.Dinner_Break != "0":
                pass
            if userCheck.Signing_Out_Time == "0" and userCheck.Tea_Break != "0":
                pass
        except:
            pass
        return render(request,'attendance.html')
    return render(request,'attendance.html')

@login_required(login_url='company:login')
def department(request):
    getUser=User.objects.get(username=request.user)
    user=UserProfile.objects.get(User=getUser)
    sendvar={
        'users':user
    }
    return render(request,'department.html',sendvar)

def login(request):
    email=request.POST.get("username")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect('company:dashbord')
       else:
            return render(request,"login.html",{'error':"Invalide user or password"})
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('company:dashbord')