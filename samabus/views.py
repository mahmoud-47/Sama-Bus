from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as log,logout as logt,authenticate
from .models import voyage,bus,reserve
from django.http import HttpResponse

def login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username = request.POST.get('username').strip()
            password = request.POST.get('password').strip()
            user=authenticate(username=username,password=password)
            if user is not None:
                myuser=User.objects.get(username=username)
                log(request,user)
                return redirect('home')
            else:
                msg="Erreur d'authentication, veuillez reessayer avec des identifiants valides"
                success = "False"
                context={'msg':msg,'success':success}
                return render(request,'Connexion.html',context)
        else:
            return render(request,'Connexion.html')
    else:
        return redirect('home')

def register(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            prenom = request.POST.get('prenom').strip()
            nom = request.POST.get('nom').strip()
            username = request.POST.get('username').strip()
            password1 = request.POST.get('password')
            password2 = request.POST.get('confirmpassword')
            email = request.POST.get('email').strip()
            if password1==password2:
                try:
                    user = User.objects.get(username=username)
                    msg = "Ce nom d'utilisateur est déja utilisé"
                    success = "False"
                    context={'msg':msg,'success':success}
                    return render(request,'Inscription.html',context)
                except:
                    try:
                        user = User.objects.get(email=email)
                        msg = "Cette adresse mail est déja utilisée"
                        success = "False"
                        context={'msg':msg,'success':success}
                        return render(request,'Inscription.html',context)
                    except:
                        user=User.objects.create_user(first_name=prenom,last_name = nom,username=username,password=password1,email=email)
                        msg = "L'inscription a été un succès. Vous pouvez vous connecter maintenant"
                        success = "True"
                        context={'msg':msg,'success':success}
                        return render(request,'Inscription.html',context)
            else:
                msg="Vos mots de passe ne sont pas identiques"
                success = "False"
                context={'msg':msg,'success':success}
                return render(request,'Inscription.html',context)
        else:
            return render(request,'Inscription.html')
    else:
        return redirect('home')

def myreserve(request,id_voyage):
    if request.user.is_authenticated:
        id_user=request.user
        myvoyage = voyage.objects.get(id = id_voyage) 
        bus_id = myvoyage.id_bus.id
        mybus = bus.objects.get(id = bus_id)
        nb_lim = mybus.place_max
        nb_entree = reserve.objects.filter(id_voyage__id_bus = mybus.id).count()
        try:
            req = reserve.objects.get(id_user = id_user,id_voyage = myvoyage)
        except:
            if nb_entree<nb_lim:
                myreserve = reserve.objects.create(
                    id_voyage = myvoyage,
                    id_user = id_user
                )
            else:
                return HttpResponse('Le bus est plein ! impossile de reserver')
            return HttpResponse('Reservation effectuée avec succes !')
        
        return HttpResponse('Oups ! vous ne pouvez pas reserver 2 fois pour un même voyage')
    else:
        return redirect('home')

def admin_gere(request):
    if request.user.is_staff:
        voyages = voyage.objects.all().filter(valide = True)
        nb = voyages.count()
        context = {"nb":nb,'voyages':voyages}
        return render(request,'Réservation.html',context)
    else:
        return redirect('login')

def annuler(request,id_voyage):
    if request.user.is_staff:
        my_voyage = voyage.objects.get(id = id_voyage)
        my_voyage.valide = False
        my_voyage.save()
        return redirect('imstaff')
    else:
        return redirect('login')

def mes_reservations(request):
    id_user = request.user
    reservs = reservation.objects.all().filter(id_user = id_user)
    context={'reservs':reservs}
    return render(request,'Profil.txt',context)

def logout(request):
    if request.user.is_authenticated:
        logt(request)
        return redirect('login')
    else:
        return redirect('login')
