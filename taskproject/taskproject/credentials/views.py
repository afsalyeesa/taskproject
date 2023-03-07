from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def home(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request,"home.html")

def new(request):
    if request.method== 'POST':
        return redirect('form')

    return render(request,"new.html")

def mechanical(request):
    if request.method == 'POST':
        return redirect('  <a href="https://en.wikipedia.org/wiki/Mechanical_engineering"></a>')
    return render(request,"mechanical.html")

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['DOB']
        Age= request.POST['Age']
        gender=request.POST['gender']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        address=request.POST['address']
        user = auth.authenticate(name=name,DOB=DOB,Age=Age,gender=gender,phoneno=phoneno,email=email,address=address)

        return redirect('submit')

    return render(request,"form.html")



def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return  redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def submit(request):

    return render(request,"submit.html")


def logout(request):
    auth.logout(request)
    return redirect('/')