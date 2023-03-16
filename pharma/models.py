from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PaysVille(models.Model):
    pays = models.CharField(max_length=40, null=True)
    ville = models.CharField(max_length=40, null=True)

class Unite(models.Model):
    typeUnite = models.CharField(max_length=40, null=True)

class Pharmacie(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    ville = models.CharField(max_length=60, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
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

class Produit(models.Model):
    designation = models.CharField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    
class Stock(models.Model):
    pharmacie = models.ForeignKey(Pharmacie, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantite_stock = models.IntegerField(null=True)
    unite = models.CharField(max_length=60, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

