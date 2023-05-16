"""gestion_pharma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from pharma import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('charger_liste_pharmacie/', views.charger_liste_pharmacie, name='charger_liste_pharmacie'),
    path('charger_produit_avec_fichier/', views.charger_produit_avec_fichier, name='charger_produit_avec_fichier'),
    path('charger_liste_tour_de_garde/', views.charger_liste_tour_de_garde, name='charger_liste_tour_de_garde'),
    path('charger_liste_tour_de_garde_com5/', views.charger_liste_tour_de_garde_com5, name='charger_liste_tour_de_garde_com5'),
    path('', include('pharma.urls'))
]
