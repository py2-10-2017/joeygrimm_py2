# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def process(request):
    price = 0
    howmany = 0
    total = 0
    print request.POST
    for key,value in request.POST.iteritems():
        if key == "quantity_shirt":
            price = 19.99
            howmany = int(value)
            total = price * howmany
            print total, key, price, howmany
            request.session['items'] = howmany
            request.session['total'] = total
        elif key == "quantity_sweatshirt":
            price = 29.99
            howmany = int(value)
            total = price * howmany
            print total, key, price, howmany
            request.session['items'] = howmany
            request.session['total'] = total
        elif key == "quantity_cup":
            price = 4.99
            howmany = int(value)
            total = price * howmany
            print total, key, price, howmany
            request.session['items'] = howmany
            request.session['total'] = total
        elif key == "quantity_book":
            price = 49.99
            howmany = int(value)
            total = price * howmany
            print total, key, price, howmany
            request.session['items'] = howmany
            request.session['total'] = total
        elif key == "quantity_computer":
            price = 2000
            howmany = int(value)
            total = price * howmany
            print total, key, price, howmany
            request.session['items'] = howmany
            request.session['total'] = total
        elif key == "quantity_hat":
            price = 15.99
            howmany = int(value)
            total = price * howmany
            print total, key, price, howmany
            request.session['items'] = howmany
            request.session['total'] = total
    return redirect('/success')

def success(request):
    context={
        "item":request.session['items'],
        "total":request.session['total'],
    }
    return render(request, 'shop/result.html', context)

def clear(request):
    request.session.flush()
    return redirect('/')