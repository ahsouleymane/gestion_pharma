from django.db import models

# Create your models here.

class Pharmacie(models.Model):

    designation = models.CharField(max_length=40, null=True)
    adresse = models.CharField(max_length=40, null=True)
    telephone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=60, null=True)
    pays  = models.CharField(max_length=60, null=True)
    ville = models.CharField(max_length=60, null=True)
    longitude = models.FloatField(max_length=40, null=True)
    latitude = models.FloatField(max_length=40, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation

