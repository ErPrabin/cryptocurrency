from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    
    return render(request,'login.html')

def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'index.html')
        
        ...
    else:
        # Return an 'invalid login' error message.
        return render(request,'register.html')

        ...
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        username=request.POST['username']

        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        return redirect('/')
    else:
        return render(request,'register.html')

