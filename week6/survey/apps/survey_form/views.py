# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, "survey_form/index.html")

def process(request):
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    context = {
        "name": request.session['name'],
        "email": request.session['email'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment']
    }
    return render(request, "survey_form/result.html", context)