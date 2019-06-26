from django.shortcuts import render
from .models import Deal
# Create your views here.
def home(request):
    deals=Deal.objects
    return render(request,'deals/home.html',{'deals':deals})

def checkout(request):
    return render(request,'checkout/checkout.html')