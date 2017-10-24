# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def index(request):
    return render(request,'login_registration/index.html')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "You've logged in.")
    return redirect('/success')

def registration(request):
    result=User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "You've registered.")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context={
        "user":User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_registration/success.html', context)