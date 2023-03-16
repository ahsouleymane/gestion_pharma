from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *

class creerutilisateurForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nom Utilisateur',
            'email': 'Email',
            'password1': 'Mot de passe',
            'password2': 'Confirmer mot de passe',
        }

class PaysVilleForm(forms.ModelForm):
    model = PaysVille
    fields = ['pays', 'ville']
    labels = {
        'pays': 'Pays',
        'ville': 'Ville',
    }

class UniteForm(forms.ModelForm):
    model = Unite
    fields = ['typeUnite']
    labels = {
        'typeUnite': 'Type Unité'
    }

class PharmacieForm(forms.ModelForm):
    class Meta:
        model = Pharmacie
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