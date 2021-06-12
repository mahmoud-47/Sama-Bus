from django.shortcuts import render
from django.http import HttpResponse
from samabus.models import *
import samabus

def home(request):
    if request.user.is_authenticated:
        voyages = samabus.models.voyage.objects.all().filter(valide=True)
        buss = samabus.models.bus.objects.all()
        nb = voyages.count()
        context = {'voyages':voyages,'nb':nb,'buss':buss}
        return render(request,'UserAccueil.html',context)
    else:
        return render(request,'Accueil.html')
