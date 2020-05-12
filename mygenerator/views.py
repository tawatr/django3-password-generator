from django.shortcuts import render

from django.http import HttpResponse

import random

# Create your views here.

def home(request):
    return render(request, 'mygenerator/home.html',
    {'password':'xxslfa'})
        # ^No folder template here
        # Provided dictionary
def about(request):
    return render(request, 'mygenerator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int( request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        characters.extend(list('@!&#*'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))


    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'mygenerator/password.html',
    {'password':thepassword} )
