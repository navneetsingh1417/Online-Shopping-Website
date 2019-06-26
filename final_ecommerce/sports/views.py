from django.shortcuts import render
from .models import Sports
# Create your views here.
def sports(request):
    sports=Sports.objects
    return render(request,'sports/sports.html',{'sports':sports})