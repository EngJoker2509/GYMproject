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
        if len(errors) > 0 :
            for key, value in errors.items():
                print(key,value)
                messages.error(request, value,extra_tags=key)
            return redirect('/')
        Register(request)
    return redirect('/login')

def login(request):
    if request.method == "POST":
        if Login(request):
            return redirect('/hola')
        else:
            return redirect('/login')
    return render(request,'login.html')

def clear(request):
    del request.session['LoginAuth']
    del request.session['userid']
    return redirect('/')


def dashboard(request):
    if request.method == 'POST':
        pass
    now = datetime.now()
    today = now.date()
    print(today)
    id=int(request.session['userid'])
    # id = 2  # gymid
    if (subScriptions.objects.filter(_to__gte=today, gymUser=id).exists()):
        list = subScriptions.objects.filter(_to__gte=today, gymUser=id)
        # print(subScriptions.objects.filter(_to__gte=today,gymUser=id)[0].participantUser.participantName)
        for user_in_gym in list:
            print(user_in_gym.participantUser.participantName)
    # return render(request,'dashboard.html',context=context)
    return HttpResponse('Scuess dashboard')


def add_participants(request):
    if request.method == 'POST':
        gym_id=request.session['userid']
        participants.add_participants(request,gym_id)
        return redirect('/participants')
    else :
        return render(request,'add_participants.html')
