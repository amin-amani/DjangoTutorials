from django.http import response
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
# from .models import MeterList , Measurements
from django.core import serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import decimal
import datetime
import pytz

@csrf_exempt
def LogoutRequest(request):
    logout(request)
    return  redirect('http://127.0.0.1:8000/')


@csrf_exempt
def LoginRequest(request):
    if request.method == 'POST': 
        user=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return  render(request,'Home.html',{})    
        else:
            return HttpResponse("Credentials are Incorrect")
    
    if request.user.is_anonymous:
        return  render(request,'Login.html',{}) 
    else:
        return  render(request,'Home.html',{})    
