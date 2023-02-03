from django.shortcuts import render
from datetime import datetime
from GYMapp.models import *

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,"aboutus.html")

def showlessons(request):
    return render(request,"lessons.html")

def showparticipants(request):
    id=int(request.session['userid'])
    now = datetime.now()
    today = now.date()
    print(today)
    # id = 2  # gymid
    if (Subscription.objects.filter(_to__gte=today, gymUser=id).exists()):
        list = Subscription.objects.filter(_to__gte=today, gymUser=id)
        # print(Subscription.objects.filter(_to__gte=today,gymUser=id)[0].participantUser.participantName)
        
        # for user_in_gym in list:
        #     print(user_in_gym.participantUser.participantName)
        context={
            'all_active_part':list
        }
    return render(request,'showparticipants.html',context=context)

    return render(request,"showparticipants.html")

def addparticipants(request):
    return render(request,"aboutus.html")

def pricing(request):
    return render(request,"pricing.html")

def addparticipant(request):
    return render(request,"addparticipant.html")

def addemployee(request):
    return render(request,"addimployee.html")

def showemployee(request):
    return render(request,"showemployee.html")

def showmhisto(request):
    return render(request,"showmhisto.html")

