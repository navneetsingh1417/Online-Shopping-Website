from django.shortcuts import render
from .models import Women
# Create your views here.
def women(request):
    women=Women.objects
    return render(request,'women/women.html',{'women':women})

