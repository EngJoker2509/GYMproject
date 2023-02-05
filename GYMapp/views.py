from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from datetime import datetime, date


def base(request):
    if request.method == 'GET':
        if 'LoginAuth' in request.session:
            return render(request, 'base.html')
    request.session['LoginAuth'] = ''
    return render(request, 'base.html')


def register(request):
    if request.method == "POST":
        errors = gymUsers.objects.basic_validtor(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                print(key, value)
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        Register(request)
    return redirect('/login')


def login(request):
    if request.method == "POST":
        if Login(request):
            return redirect('/dashboard/showparticipants')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def call_about(request):
    return render(request, "about.html")

def call_pricing(request):
    return render(request, "pricing.html")

def call_contact(request):
    return render(request, "contact.html")
