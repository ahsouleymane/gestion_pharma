from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from pharma.forms import *
from pharma.models import *

# Create your views here.

def acceuil(request):
    context = {}
    return render(request, 'pharma/acceuil.html', context)

def ajouter_pharmacie(request):
    form = PharmacieForm
    form1 = creerutilisateurForm

    if request.method == 'POST':
        form1 = creerutilisateurForm(request.POST)
        form = PharmacieForm(request.POST)

        if form.is_valid() and form1.is_valid():
            instance1 = form1.save(commit = False)
            instance = form.save(commit = False)

            if instance is not None:
                if instance1 is not None:
                    instance1.save()
                    instance.save()
                    
    context = {'form': form, 'form1': form1}
    return render(request, 'pharma/ajouter_pharmacie_form.html', context)

def editer_pharmacie(request):
    pass

def supprimer_pharmacie(request):
    pass

def charger_produit_avec_fichier(request):
    pass

def ajouter_stock(request):
    pass

def mettre_a_jour_stock(request):
    pass

def rechercher_produit_en_fonction_de_pharmacie_et_stock(request):
    pass
