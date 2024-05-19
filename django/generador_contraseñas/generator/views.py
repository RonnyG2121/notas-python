from django.shortcuts import render

import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password_gen(request):
    generated_password = ''
    charapters = ['abcdefghijklmnopqrstuvwxyz']

    for charapter in charapters:
        generated_password += charapter
        


    return render(request, 'generator/password_gen.html')


def about(request):
    return render(request, 'generator/about.html')
