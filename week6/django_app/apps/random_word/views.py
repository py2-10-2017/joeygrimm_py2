# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.utils.crypto import get_random_string
 


# Create your views here.
def index(request):
    try:
        request.session['attempts'] += 1
    except:
        if not 'attempts' in request.session:
            request.session['attempts'] = 0

    request.session['word'] = get_random_string(14)

    return render(request, "random_word/index.html")

def generate(request):
    return redirect("/")

def reset(request):
    request.session['attempts'] = 0
    return redirect("/", request.session['attempts'])


