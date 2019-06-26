from django.shortcuts import render
from .models import Electronics
# Create your views here.
def electronics(request):
    electronics=Electronics.objects
    return render(request,'electronics/electronics.html',{'electronics':electronics})
