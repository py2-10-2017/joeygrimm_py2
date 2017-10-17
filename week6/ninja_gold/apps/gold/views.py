# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import random

from datetime import datetime

# Create your views here.
def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    elif 'gold' in request.session:
        pass
    print request.session['gold']
    return render(request,"gold/index.html")


def process_money(request):
    newgold = 0
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    building = request.POST['building']

    if request.POST['building'] == 'farm':
        newgold = random.randint(10, 20)
        request.session['gold'] += newgold
        request.session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, request.session['gold'], time))

    elif request.POST['building'] == 'cave':
        newgold = random.randint(5, 10)
        request.session['gold'] += newgold
        request.session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, request.session['gold'], time))

    elif request.POST['building'] == 'house':
        newgold = random.randint(2, 5)
        request.session['gold'] += newgold
        request.session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, request.session['gold'], time))

    elif request.POST['building'] == 'casino':
        newgold = random.randint(-50, 50)
        request.session['gold'] += newgold
        if request.session['gold'] <= 0:
           request.session['gold'] = 0 
           request.session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} negative gold pieces. Your gold will be reset to 0. {}".format(building, newgold, request.session['gold'], time))
        else:
            request.session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, request.session['gold'], time))

    print "Added ", newgold," to my gold. I now have...", request.session['gold']
    return redirect('/')

def reset(request):

    if request.POST['reset']:
        request.session['gold'] = 0
        request.session['activity'] = []
    return redirect('/')
