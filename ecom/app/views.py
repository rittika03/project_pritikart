from django.shortcuts import render, redirect# type: ignore
from .models import Users
from django.contrib.auth.hashers import make_password,check_password # type: ignore
from django.contrib.auth import login as auth_login # type: ignore

# Create your views here.
def home(req):
    return render(req,'home.html')

def home2(req):
    return render(req,'home2.html')


def login(req):
    if req.method=='POST':
        email=req.POST['email']
        password=req.POST['password']
        try:
            user=Users.objects.get(email=email)
            if check_password(password,user.password):
                auth_login(req,user)
                return redirect('home2')
            else:
                return render(req,'login.html',{'error':'Invalid Password'})
        except Users.DoesNotExist:
            return render(req,'login.html',{'error':'Invalid Email'})
    else:
      return render(req,'login.html')

def signup(req):
    if req.method == 'POST':
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        hashed_password= make_password(password)
        user= Users(username=username,email=email,password=hashed_password)
        user.save()
        return redirect('login') # Redirect to the home page
    else:
      return render(req, 'signup.html')

def my_profile(req):
    return render(req,'my_profile.html')

def billing(req):
    return render(req,'billing.html')

def skincare(req):
    return render(req,'skincare.html')

def makeup(req):
    return render(req,'makeup.html')

def clothes(req):
    return render(req,'clothes.html')

def accessories(req):
    return render(req,'accessories.html')