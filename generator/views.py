from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    
    return render(request, 'generator/index.html')

def passowrd(request):
    length = int(request.GET.get('length'))

    letters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))
    if request.GET.get('capital'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        letters.extend(list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))

    

    
    thepassword = ''
    for i in range(length):
        thepassword +=  random.choice(letters)
    
    return render(request, 'generator/password.html', {"password":thepassword})
    

# Create your views here.
