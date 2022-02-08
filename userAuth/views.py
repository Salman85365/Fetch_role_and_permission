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
