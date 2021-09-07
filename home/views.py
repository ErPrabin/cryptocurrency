from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='/account/login/')
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')