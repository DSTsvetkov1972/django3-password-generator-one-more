from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def view_home(request):
    return render(request, "generator/template_home.html")

def view_password(request):    
    characters = list('abcdefgijklmnopqrstuvwxyz')

    if request.GET.get('uppercase') == 'on':
        characters.extend('ABCDEFGIJKLMNOPQRSTUVWZYZ')

    if request.GET.get('number') == 'on':
        characters.extend('0123456789')    
        
    if request.GET.get('special') == 'on':
        characters.extend('!@#$%^&*()_+') 

    length = int(request.GET.get('length', 2))
    
    thepassword = ''
    for x in range(0,length):
        thepassword += random.choice(characters)
    
    #print(characters)
 
    return render(request, "generator/template_generator.html", {"password":thepassword})

def view_about(request):
    return render(request, "generator/template_about.html")