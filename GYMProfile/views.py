from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,"aboutus.html")

def showlessons(request):
    return render(request,"lessons.html")

def showparticipants(request):
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

