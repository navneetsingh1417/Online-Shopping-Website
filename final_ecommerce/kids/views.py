from django.shortcuts import render
from .models import Kids
# Create your views here.
def kids(request):
    kids=Kids.objects
    return render(request,'kids/kids.html',{'kids':kids})
    