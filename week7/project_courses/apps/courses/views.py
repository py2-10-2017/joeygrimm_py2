# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context ={
        "courses":Course.objects.all()
    }
    return render(request,"courses/index.html", context)

def create(request):
    errors= Course.objects.validate_course(request.POST)
    if errors:
        for fail in errors:
            messages.error(request, fail)
        return redirect("/courses")
    Course.objects.create(
        name=request.POST['name'],
        desc=request.POST['desc']
    )
    print "no errors with create"
    return redirect("/courses")

def deleteshow(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, "courses/destroy.html", context)

def destroy(request, course_id):
    course_destroy=Course.objects.get(id=course_id)
    course_destroy.delete()
    return redirect("/courses")