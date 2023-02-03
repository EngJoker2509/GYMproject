from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from GYMapp.models import *

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "aboutus.html")


def showlessons(request):
    return render(request, "lessons.html")


def showparticipants(request):
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


def addparticipants(request):
    if request.method == 'POST':
        gym_id = request.session['userid']
        participants.add_participants(request, gym_id)
        _part = participants.objects.last()
        return redirect(f'/dashboard/addsup/{_part.id}')
    else:
        return render(request, 'addparticipant.html')


def pricing(request):
    return render(request, "pricing.html")


# def addparticipant(request):
#     return render(request, "addparticipant.html")


def addsup(request, id):
    if request.method == 'POST':
        now = datetime.now()
        today = now.date()
        gym_id = request.session['userid']
        par_id = int(id)
        _to = today+timedelta(days=30)
        Subscription.add_subscription(request, gym_id, par_id, _to)
        return redirect('/dashboard/showparticipants')
    else:
        context = {
            'id': id
        }
        return render(request, 'addsup.html', context=context)


def showemployee(request):
    return render(request, "showemployee.html")


def showmhisto(request, id):
    participant = participants.objects.get(id=id)

    context = {
        "user": participant,
    }
    return render(request, "showmhisto.html", context)
