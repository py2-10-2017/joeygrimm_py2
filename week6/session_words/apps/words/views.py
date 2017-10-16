# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import pytz
from django.utils import timezone
from django.shortcuts import render, redirect, HttpResponse

'''
    Make a form, which allows you to post a new word.
    Make it so you can choose between three colors for the word
    Also, a check box for Font size of the word.
    Have a button which posts the information. 
    Once the button is pressed, it needs to reload the page. 
    The session information will be to the left side of the screen. 
    Also, a  button will be on the left side of the screen, which can clear all session data
    It appears as if you'll need at least 4 views function.
    You also have to define several classes to contain the styling information of the user
'''


# Create your views here.
def index(request):
    return render(request, "words/index.html")

def process(request):
    new_words = {}
    for key, value in request.POST.iteritems():
        if key == "font":
            new_words['font'] = "font"
        elif key != "font":
            new_words[key] = value
    new_words['time'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['word']
    except KeyError:
        request.session['word'] = []

    temp_list = request.session['word']
    temp_list.append(new_words)
    request.session['word']=temp_list
  
    return redirect('/')

def delete(request):
    request.session.flush()
    return redirect('/')