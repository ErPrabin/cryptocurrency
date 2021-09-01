from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')