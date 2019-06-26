from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import admin

# Create your views here.
def signup(request):
    if request.method== 'POST':
        try:
            user=User.objects.get(username==request.POST['username'])
            return render(request,'accounts/signup.html',{'error':'user already exists'})
        except User.DoesNotExist:
            user=User.objects.create_user(request.POST['username'],password=requestPOST['password1'])
            auth.login(request,user)
            return redirect('home')
    else:
        pass

    return render(request,'accounts/signup.html')