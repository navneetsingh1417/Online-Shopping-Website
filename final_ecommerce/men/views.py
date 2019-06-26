from django.shortcuts import render
from .models import Men
# Create your views here.
def men(request):
    men=Men.objects
    return render(request,'men/men.html',{'men':men})