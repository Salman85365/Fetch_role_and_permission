from django.shortcuts import render,HttpResponse
from django.urls import reverse
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import User
from django.shortcuts import redirect
from django.contrib import auth

def authenticate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user_obj = User.objects.get(username=username)
        except:
            return HttpResponse("User not existed")
        result = user_obj.check_password(password)
        if not result:
            return HttpResponse("Invalid password")
        auth.authenticate(user_obj)
        context = {
            "username": user_obj.username,
            "user_role": user_obj.role,
            "permission": list(user_obj.user_permissions.values_list("name", flat=True))
        }
        return render(request, "user_role_and_perm.html",context)
    return render(request,"login.html")


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username Exists! Try another One")
            else:
                if User.objects.filter(email=email).exists():
                    return HttpResponse("Email already Exists! Try another One")
                else:
                    user = User.objects.create_user(username=username,
                                                    email=email, password=password)
                    user.save()
                    return render(request,"register_success.html")
        else:
            return HttpResponse("Password do not matched!")
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
