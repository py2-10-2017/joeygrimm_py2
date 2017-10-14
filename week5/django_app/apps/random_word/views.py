# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.utils.crypto import get_random_string
 


# Create your views here.
def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request, "random_word/index.html")

def generate(request):
    request.session['tries'] += 1  
    request.session['word'] = get_random_string(14)
    return redirect('/random_word')

