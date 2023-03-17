from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pharma.forms import *
from pharma.models import *
from .resources import ProduitResource
from tablib import Dataset
from django.http import HttpResponse

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

            return redirect('/list_pharmacie/')
                    
    context = {'form': form, 'form1': form1}
    return render(request, 'pharma/ajouter_pharmacie_form.html', context)

def list_pharmacie(request):
    pharmacie = Pharmacie.objects.all()
    context = {'pharmacie': pharmacie}
    return render(request, 'pharma/list_pharmacie.html', context)

def editer_pharmacie(request, pk):
    pharmacie = Pharmacie.objects.get(id=pk)
    form = PharmacieForm(instance = pharmacie)

    if request.method == 'POST':
        form = PharmacieForm(request.POST, instance = pharmacie)

        if form.is_valid():
            form.save()
            return redirect('/list_pharmacie/')
                    
    context = {'form': form}
    return render(request, 'pharma/editer_pharmacie_form.html', context)

def supprimer_pharmacie(request, pk):
    pharmacie = Pharmacie.objects.get(id=pk)

    if request.method == 'POST':
        pharmacie.delete()  
        return redirect('/list_pharmacie/')
    
    context = {'pharmacie': pharmacie}
    return render(request, 'pharma/supprimer_pharmacie_form.html', context)

def charger_produit_avec_fichier(request):
    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()
        nouveau_produit = request.FILES['monFichier']

        if not nouveau_produit.name.endswith('xlsx'):
            messages.info(request, 'Mauvais format !!!')
            return render(request, 'pharma/charger_produit_form.html')
        
        imported_data = dataset.load(nouveau_produit.read(), format='xlsx')
        for data in imported_data:
            value = Produit(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        return redirect('/list_produit/')
    return render(request, 'pharma/charger_produit_form.html')

def list_produit(request):
    produit = Produit.objects.all()
    context = {'produit': produit}
    return render(request, 'pharma/list_produit.html', context)

def ajouter_stock(request):
    pass

def mettre_a_jour_stock(request):
    pass

def rechercher_produit_en_fonction_de_pharmacie_et_stock(request):
    pass
