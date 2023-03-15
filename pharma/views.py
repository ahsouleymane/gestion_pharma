from django.shortcuts import render, redirect

# Create your views here.

def acceuil(request):
    return redirect(request, 'pharma/acceuil.html')

def ajouter_pharmacie(request):
    pass

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
