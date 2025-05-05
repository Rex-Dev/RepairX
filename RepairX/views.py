from django.shortcuts import render
from .models import User,Employee,Service,Repair,Spares,Vehicle,UserVehicle,Appoinments


# Create your views here.
def home(request):
    return render(request,'home.html')

#User Registration
def usereg(request):
    if request.method=='POST':
        userphone=request.POST.get('user_phn')
        phone=User.objects.filter(userphone=userphone)
        if phone:
            return render(request,'User/useregister.html')
        else:
            username=request.POST.get('user_name')
            useremail=request.POST.get('user_email')
            userlocation=request.POST.get('user_loc')
            userpassword=request.POST.get('user_pswd')
            userage=request.POST.get('user_age')
            user = User.objects.create(
                username=username,
                userphone=userphone,
                useremail=useremail,
                userlocation=userlocation,
                userpassword=userpassword,
                userage=userage
            )
            user.save()
            return render(request,'User/userlogin.html')
    return render(request,'User/useregister.html')

#User Login
def userlogin(request):
    if request.method=='POST':
        userphone=request.POST.get('phno')
        userpassword=request.POST.get('pswd')
        
        check=User.objects.filter(userphone=userphone,userpassword=userpassword).first()
        if check:
            return render(request,'home.html')
        else:
            return render(request,'User/userlogin.html')
    return render(request,'User/userlogin.html')

#Employee login
def emplogin(request):
    if request.method=='POST':
        empid=request.POST.get('id')
        empassword=request.POST.get('pswd')
        check=Employee.objects.get(empid=empid,empassword=empassword)
        if check:
            return render(request,'home.html')
        else:
            return render(request,'emplogin.html')
    return render(request,'emplogin.html')