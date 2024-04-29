from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, team

# Create your views here.
# def home(request):
#     return HttpResponse("Home Page")

def home(request):
    return render(request, "home.html")

#admin pass: Devutty@1

def index(request):
    demo=Place.objects.all()
    rev = team.objects.all()
    return render(request,'index.html',{'plc':demo,'tem':rev})