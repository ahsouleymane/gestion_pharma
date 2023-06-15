from django.db import models
from django.contrib.auth.models import User
from gestion_pharma import settings

# Create your models here.

class PaysVille(models.Model):
    pays = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.pays + ' ' + self.ville

class Unite(models.Model):
    typeUnite = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.typeUnite

class Groupe(models.Model):
    libelle = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.libelle

class Pharmacie(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=60, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.utilisateur.username
    
    def save(self, *args, **kwargs):
        try:
            self.utilisateur
        except:
            self.utilisateur = User.objects.last()
        super().save(*args, **kwargs)

class PharmacieGarde(models.Model):
    pharmacie = models.CharField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, default=0)
    longitude = models.FloatField(max_length=40, default=0)
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.pharmacie

class Produit(models.Model):
    designation = models.CharField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designation

class Stock(models.Model):
    pharmacie = models.ForeignKey(PharmacieGarde, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantite_stock = models.IntegerField(null=True, default=0)
    unite = models.ForeignKey(Unite, null=True, on_delete=models.SET_NULL)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pharmacie) + ' à pour stock ' + str(self.quantite_stock)

class TourGarde(models.Model):
    debut_tour = models.DateField(auto_now_add=False, auto_now=False, null=True)
    fin_tour = models.DateField(auto_now_add=False, auto_now=False, null=True)
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Du ' + str(self.debut_tour) + ' au ' + str(self.fin_tour)
    
class TourGardeCom5(models.Model):
    debut_tour = models.DateField(auto_now_add=False, auto_now=False, null=True)
    fin_tour = models.DateField(auto_now_add=False, auto_now=False, null=True)
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Du ' + str(self.debut_tour) + ' au ' + str(self.fin_tour)
    
class Commande(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    pharmacie_ou_vient_la_commande = models.CharField(max_length=40, null=True)
    produit_commandE = models.CharField(max_length=60, null=True)
    quantite_produit = models.IntegerField(null=True, default=0)
    unite_de_la_commande = models.CharField(max_length=40, null=True)
    valider = models.BooleanField(default=False, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Pharmacie: ' + str(self.pharmacie_ordre) + ' Produit: ' + str(self.produit_ordre) + ' Quantité Produit: ' +  str(self.quantite_produit) + ' ' + str(self.unite_ordre)

    @property
    def total_produit(self):
        total = 0
        if self.valider:
            total = sum(id)

