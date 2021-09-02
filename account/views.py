from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return redirect('/account/login/')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            response = redirect('/')
            # log the user in
            return response
        return redirect('/account/login/')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/account/login/')
    # Redirect to a success page.
