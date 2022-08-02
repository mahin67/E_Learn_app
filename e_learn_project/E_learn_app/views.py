from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user,logout
# Create your views here.

def home_page(request):
    return render(request,"index.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print('username---',username)
        print('password---',password)

        user = authenticate(request,username=username,password=password)

        if user is not None:
            print('hello',user)
            login_user(request,user)
            print('login success')
            return redirect('home')
        else:
            print('hello failed',user)
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:           
        return render(request, 'login.html')
