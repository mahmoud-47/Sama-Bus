from django.db import models
from django.contrib.auth.models import User

class bus(models.Model):
    matricule = models.CharField(max_length=30,unique=True)
    place_max = models.IntegerField(null=True)
    def __str__(self):
        return self.matricule
    

class voyage(models.Model):
    depart = models.CharField(max_length=50)
    arrivee = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    heure = models.CharField(max_length=20)
    valide = models.BooleanField(default=True,null=True)
    id_bus = models.ForeignKey(bus, null=True, on_delete=models.CASCADE)
    prix = models.CharField(max_length=5,null=True)
    def __str__(self):
        return self.depart[:3]+'.. - '+self.arrivee[:3]+'..'
    

class reserve(models.Model):
    date = models.DateTimeField(auto_now_add=True,null=True)
    id_voyage = models.ForeignKey(voyage,on_delete=models.CASCADE,null=True)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
