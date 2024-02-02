from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def Register(req):
    if req.method=='POST':
        username=req.POST['username']
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        email=req.POST['email']
        password=req.POST['password']
        c_password=req.POST['c_password']
        print(username,first_name,last_name,email,password,c_password)
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"Email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                # return redirect('login')
                user=auth.authenticate(username=username,password=password)
                auth.login(req,user)
                return redirect('/')
        else:
            messages.info(req,"password didnt match")
            return redirect('register')
    return render(req,'register.html')

def Login(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            req.session['user']=user.id
            return redirect('/')
        else:
            messages.info(req,"invalid user")
            return redirect('login')
    return render(req,'login.html')

def Logout(req):
    auth.logout(req)
    req.session.flush()
    return redirect('/')