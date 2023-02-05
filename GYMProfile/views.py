from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from GYMapp.models import *

# Create your views here.
from django.shortcuts import render


def show_lessons(request):
    if not "userid" in request.session:
        return redirect('/')
    return render(request, "lessons.html")


def show_participants(request):
    if not "userid" in request.session:
        return redirect('/')
    id = int(request.session['userid'])
    now = datetime.now()
    today = now.date()
    print(today)
    Subscription.update_active(today,id)
    if request.method == 'POST':
        name = str(request.POST['search'])
        if len(name) == 0:
            if (Subscription.objects.filter(gymUser=id).exists()):
                list = Subscription.objects.filter(gymUser=id)
                # print(Subscription.objects.filter(to_date__gte=today,gymUser=id)[0].participantUser.participantName)
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
            if (Subscription.objects.filter(gymUser=id, participantUser__participantName__startswith=name).exists()):
                list = Subscription.objects.filter(gymUser=id, participantUser__participantName__startswith=name)
                context = {
                    'all_active_part': list
                }
            else:
                context = {
                    'all_active_part': ''
                }
    else:
        if (Subscription.objects.filter(gymUser=id).exists()):
            list = Subscription.objects.filter(gymUser=id)
            # print(Subscription.objects.filter(to_date__gte=today,gymUser=id)[0].participantUser.participantName)
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
    if not "userid" in request.session:
        return redirect('/')
    if request.method == 'POST':
        gym_id = request.session['userid']
        participants.add_participants(request.POST, gym_id)
        return redirect('/dashboard/showparticipants')
    else:
        return render(request, 'addparticipant.html')


def add_employee(request):
    if not "userid" in request.session:
        return redirect('/')
    if request.method == 'POST':
        gym_id = request.session['userid']
        Employee.add_employee(request.POST, gym_id)
        print("added successfully")
        return redirect('/dashboard/showemployee')
    else:
        return render(request, 'addemployee.html')


def show_employee(request):
    if not "userid" in request.session:
        return redirect('/')
    id = int(request.session['userid'])
    if request.method == 'POST':
        name = str(request.POST['search'])
        if len(name) == 0:
            if (Employee.objects.filter(gym=id).exists()):
                gym = Employee.objects.filter(gym=id)
                # print(gym[0].employees.name)
                # print(gym[0].name)
                context = {
                    "gym": gym
                }
            else:
                context = {
                    "gym": ''
                }
        else:
            if (Employee.objects.filter(gym=id, name__startswith=name)):
                gym = Employee.objects.filter(
                    gym=id, name__startswith=name)
                context = {
                    "gym": gym
                }
            else:
                context = {
                    "gym": ''
                }
        return render(request, "showemployee.html", context)
    else:
        if (Employee.objects.filter(gym=id).exists()):
            gym = Employee.objects.filter(gym=id)
            context = {
                "gym": gym
            }
        else:
            context = {
                "gym": ''
            }
        return render(request, "showemployee.html", context)


def show_mhisto(request, id):
    if not "userid" in request.session:
        return redirect('/')
    participant = participants.objects.get(id=id)
    context = {
        "user": participant,
    }
    return render(request, "showmhisto.html", context)


def signout_user(request):
    if not "userid" in request.session:
        return redirect('/')
    del request.session['userid']
    del request.session['username']
    return redirect("/")

def delete_employee(request,id):
    if not "userid" in request.session:
        return redirect('/')
    Employee.delete_employee(id)

    return redirect("/dashboard/showemployee")

def userprofile(request,id):
    context={
        'newpartis':participants.objects.get(id=id)
    }


    return render(request,"userprofile.html",context)
    
