from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class creerPharmacieAndAccountForm(UserCreationForm):
    model = User
    fields = ['username', 'email', 'designation', 'adresse', 
              'telephone', 'ville', 'longitude', 'latitude',
              'password1', 'password2 ']
    labels = {
        'username': 'Nom Utilisateur',
        'email': 'Email',
        'designation': 'Désignation',
        'adresse': 'Adresse',
        'telephone': 'Téléphone',
        'ville': 'Ville',
        'longitude': 'Longitude',
        'latitude': 'Latitude',
        'password1': 'Mot de passe',
        'password2': 'Confirmer mot de passe',
    }

class PharmacieAndAccountForm(forms.ModelForm):
    model = PharmacieAndAccount
    fields = ['designation', 'adresse', 'telephone', 'ville', 'longitude', 'latitude',]
    labels = {
        'designation': 'Désignation',
        'adresse': 'Adresse',
        'telephone': 'Téléphone',
        'ville': 'Ville',
        'longitude': 'Longitude',
        'latitude': 'Latitude',
    }

class ProduitForm(forms.ModelForm):
    model = Produit
    fields = ['designation']
    labels = {
        'designation': 'Désignation'
    }

class StockForm(forms.ModelForm):
    model = Stock
    fields = ['pharmacie', 'produit', 'quantite_stock', 'unite']
    labels = {
        'pharmacie': 'Pharmacie',
        'produit': 'Produit',
        'quantite_stock': 'Quantite Stock',
        'unite': 'Unité'
    }