from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from GYMapp.models import *

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "aboutus.html")


def show_lessons(request):
    return render(request, "lessons.html")


def show_participants(request):
    id = int(request.session['userid'])
    now = datetime.now()
    today = now.date()
    print(today)
    if request.method == 'POST':
        name = str(request.POST['search'])
        if len(name) == 0:
            # id = 2  # gymid
            if (Subscription.objects.filter(_to__gte=today, gymUser=id).exists()):
                list = Subscription.objects.filter(_to__gte=today, gymUser=id)
                # print(Subscription.objects.filter(_to__gte=today,gymUser=id)[0].participantUser.participantName)

                # for user_in_gym in list:
                #     print(user_in_gym.participantUser.participantName)

                context = {
                    'all_active_part': list
                }
            else:
                context = {
                    'all_active_part': ''
                }
        else:
            if (Subscription.objects.filter(_to__gte=today, gymUser=id, participantUser__participantName__startswith=name).exists()):
                list = Subscription.objects.filter(
                    _to__gte=today, gymUser=id, participantUser__participantName__startswith=name)
                context = {
                    'all_active_part': list
                }
            else:
                context = {
                    'all_active_part': ''
                }
    else:
        if (Subscription.objects.filter(_to__gte=today, gymUser=id).exists()):
            list = Subscription.objects.filter(_to__gte=today, gymUser=id)
            # print(Subscription.objects.filter(_to__gte=today,gymUser=id)[0].participantUser.participantName)

            # for user_in_gym in list:
            #     print(user_in_gym.participantUser.participantName)

            context = {
                'all_active_part': list
            }
        else:
            context = {
                'all_active_part': ''
            }
    return render(request, 'showparticipants.html', context=context)


def add_participants(request):
    if request.method == 'POST':
        gym_id = request.session['userid']
        participants.add_participants(request.POST, gym_id)
        return redirect('/dashboard/showparticipants')
    else:
        return render(request, 'addparticipant.html')
    
def add_employee(request):
    if request.method == 'POST':
        gym_id = request.session['userid']
        Employee.add_employee(request.POST, gym_id)
        print("added successfully")
        return redirect('/dashboard/showemployee')
    else:
        return render(request, 'addemployee.html')


def pricing(request):
    return render(request, "pricing.html")


def show_employee(request):
    id= request.session["userid"]
    gym=gymUsers.objects.get(id=id)
    context = {
        "gym": gym,
    }

    return render(request, "showemployee.html",context)


def show_mhisto(request, id):
    participant = participants.objects.get(id=id)

    context = {
        "user": participant,
    }
    return render(request, "showmhisto.html", context)

def signout_user(request):

    if not "userid"  in request.session:
        return redirect('/')
    del request.session['userid']
    del request.session['username']
    
    return redirect("/")
