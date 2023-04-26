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
    class Meta:
        model = PaysVille
        fields = ['pays', 'ville']
        labels = {
            'pays': 'Pays',
            'ville': 'Ville',
        }

class UniteForm(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ['typeUnite']
        labels = {
            'typeUnite': 'Type Unité'
        }

class PharmacieForm(forms.ModelForm):
    class Meta:
        model = Pharmacie
        fields = ['designation', 'adresse', 'telephone', 'ville', 'latitude', 'longitude']
        labels = {
            'designation': 'Désignation',
            'adresse': 'Adresse',
            'telephone': 'Téléphone',
            'ville': 'Ville',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['designation']
        labels = {
            'designation': 'Désignation'
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['pharmacie', 'produit', 'quantite_stock', 'unite']
        labels = {
            'pharmacie': 'Pharmacie',
            'produit': 'Produit',
            'quantite_stock': 'Quantite Stock',
            'unite': 'Unité'
        }

class GroupeForm(forms.ModelForm):
    class Meta:
        model = Groupe
        fields = ['libelle']
        labels = {
            'libelle': 'Groupe'
        }

class PharmacieGardeForm(forms.ModelForm):
    class Meta:
        model = PharmacieGarde
        fields = ['pharmacie', 'latitude', 'longitude', 'groupe']
        labels = {
            'pharmacie': 'Pharmacie',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'groupe': 'Groupe de garde'
        }

    def __init__(self, *args, **kwargs):
            super(PharmacieGardeForm,self).__init__(*args, **kwargs)
            self.fields['groupe'].empty_label = "Choisir"
 
class TourGardeForm(forms.ModelForm):
    class Meta:
        model = TourGarde
        fields = ['debut_tour', 'fin_tour', 'groupe']
        labels = {
            'debut_tour': 'Début Tour',
            'fin_tour': 'Fin Tour',
            'groupe': 'Groupe de garde',
        }

    def __init__(self, *args, **kwargs):
            super(TourGardeForm,self).__init__(*args, **kwargs)
            self.fields['groupe'].empty_label = "Choisir"
