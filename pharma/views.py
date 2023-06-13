from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import date
from pharma.filters import *

from pharma.forms import *
from pharma.models import *
from .utils import *

from tablib import Dataset

from geopy.geocoders import Nominatim
from geopy.distance import geodesic # this fonction calculate distance

import socket
import folium
import requests
import json, urllib
import datetime

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
        #produit_resource = ProduitResource()
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

def localisation_et_calcule_de_distance(request):
    #### Distances calculation

    # Initial values
    distance = None
    # destination = None

    # Get IP adress using json method1
    # r = requests.get('https://get.geojs.io/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ip_add = ip_request.json()['ip']
    print(ip_add)

    # Get ip data using json method2
    ip = requests.get('https://api.ipify.org?format=json')
    """ ip_data = json.loads(ip.text)
    print(ip_data) """

    # Get private IP adress using socket
    """ hostName = socket.gethostname()
    print(hostName)
    ipAddr = socket.gethostbyname(hostName)
    print(ipAddr) """

    url = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    #print(geo_data)

    # Location coordinates
    x_lat = float(geo_data['latitude'])
    x_lon = float(geo_data['longitude'])
    #print(x_lat, x_lon)

    pointA = (x_lat, x_lon)

    geolocator = Nominatim(user_agent='pharma')
    country, city, lat, lon = get_geo(ip_add)
    location = geolocator.geocode(city)

    
    number_of_location = PharmacieGarde.objects.all().count()
    #print('Number of location: ', number_of_location)

    locations = []

    parcourt = 0
    while parcourt < number_of_location:

        locations = PharmacieGarde.objects.values_list('pharmacie', flat=True)
        parcourt += 1

    #print(locations)


    latitudes = []
    longitudes = []

    parcourt = 0
    while parcourt < number_of_location:

        latitudes = PharmacieGarde.objects.values_list('latitude', flat=True)
        longitudes = PharmacieGarde.objects.values_list('longitude', flat=True)

        parcourt += 1

    #print(latitudes)
    #print(longitudes)

    distances = []

    parcourt = 0
    while parcourt < number_of_location and parcourt < len(latitudes) and parcourt < len(longitudes):
        
        d_lat = latitudes[parcourt]
        d_lon = longitudes[parcourt]

        pointB = (d_lat, d_lon)

        # calculate distance
        distance = round(geodesic(pointA, pointB).km, 2)

        distances.append(locations[parcourt] + ': ' + str(distance) + ' Km')

        parcourt += 1



    print("\n")
    # print("List of distances for all location and distances:\n")

    m = folium.Map(width=1600, height=600, location=get_center_coordinates(x_lat, x_lon), zoom_start=14)

    # Location marker
    folium.Marker([x_lat, x_lon], tooltip='click here for more', popup=city['city'], 
                    icon=folium.Icon(color='red')).add_to(m)
    
    pharmacies = PharmacieGarde.objects.all()

    for pharmacie in pharmacies:
        coordinates = (pharmacie.latitude, pharmacie.longitude)
        folium.Marker(coordinates, popup=pharmacie.pharmacie,
                      tooltip='Cliquer ici pour afficher le nom de la pharmacie', 
                      icon=folium.Icon(color='purple')).add_to(m)

    # Get HTML representation of map object
    m = m._repr_html_()

    context = {'map': m, 'distances': distances}
    return render(request, 'pharma/afficher_distance_pharmacie.html', context)

def charger_liste_pharmacie(request):
    if request.method == 'POST':
        dataset = Dataset()
        nouvelle_liste = request.FILES['monFichier']

        if not nouvelle_liste.name.endswith('xlsx'):
            messages.info(request, 'Mauvais format !!!')
            return render(request, 'pharma/charger_pharmacie_form.html')
        
        imported_data = dataset.load(nouvelle_liste.read(), format='xlsx')
        for data in imported_data:
            value = PharmacieGarde(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
            )
            value.save()
        return redirect('/list_pharmacie_garde/')
    return render(request, 'pharma/charger_pharmacie_form.html')

@csrf_exempt
def editer_pharmacie_garde_live(request):
    id = request.POST.get('id', '')
    type = request.POST.get('type', '')
    value = request.POST.get('value', '')
    pharmacie_garde = PharmacieGarde.objects.get(id=id)

    if type == "groupe":
        pharmacie_garde.groupe = value

    pharmacie_garde.save()
    return JsonResponse({"Reussi":"Edité"})

def liste_pharmacie_garde(request):
    pharmacie_garde = PharmacieGarde.objects.all()
    context = {'pharmacie_garde': pharmacie_garde}
    return render(request, 'pharma/list_pharmacie_garde.html', context)


def charger_liste_tour_de_garde(request):
    if request.method == 'POST':
        dataset = Dataset()
        nouvelle_liste = request.FILES['monFichier']

        if not nouvelle_liste.name.endswith('xlsx'):
            messages.info(request, 'Mauvais format !!!')
            return render(request, 'pharma/charger_liste_garde_form.html')
        
        imported_data = dataset.load(nouvelle_liste.read(), format='xlsx')
        for data in imported_data:
            value = TourGarde(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        return redirect('/liste_tour_garde/')
    return render(request, 'pharma/charger_liste_garde_form.html')

def liste_tour_garde(request):
    tour_garde = TourGarde.objects.all()
    context = {'tour_garde': tour_garde}
    return render(request, 'pharma/liste_tour_garde.html', context)

def charger_liste_tour_de_garde_com5(request):
    if request.method == 'POST':
        dataset = Dataset()
        nouvelle_liste = request.FILES['monFichier']

        if not nouvelle_liste.name.endswith('xlsx'):
            messages.info(request, 'Mauvais format !!!')
            return render(request, 'pharma/charger_liste_garde_com5_form.html')
        
        imported_data = dataset.load(nouvelle_liste.read(), format='xlsx')
        for data in imported_data:
            value = TourGardeCom5(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        return redirect('/liste_tour_garde_com5/')
    return render(request, 'pharma/charger_liste_garde_com5_form.html')

def liste_tour_garde_com5(request):
    tour_garde = TourGardeCom5.objects.all()
    context = {'tour_garde': tour_garde}
    return render(request, 'pharma/liste_tour_garde_com5.html', context)

def liste_pharmacie_garde(request):

    ########## Alternance Garde ##########

    tour = TourGarde.objects.values_list()

    # Convertir le QuerySet en List de tuple
    liste_de_tuple = [t for t in tour]
    #print(liste_de_tuple)

    # Compter le nombre de ligne dans la table
    nombre_tour = TourGarde.objects.all().count()

    parcourt = 0
    while parcourt < nombre_tour:

        # Parcourir la liste tuple par tuple
        un_tuple = liste_de_tuple[parcourt]
       
        #print(un_tuple)

        # Convertir le tuple en List
        une_liste = [d for d in un_tuple]
        #print(une_liste)

        # Récuperer les elements de la liste à travers leur indice
        debut_tour = une_liste[1]
        #print(debut_tour)

        fin_tour = une_liste[2]
        #print(fin_tour)

        groupe = une_liste[3]
        #print(groupe)
       
        if date.today() >= debut_tour and date.today() <= fin_tour:
            as_debut_tour = debut_tour
            as_fin_tour = fin_tour
            pharmacie = PharmacieGarde.objects.filter(groupe=groupe).values_list('pharmacie', flat=True)
            pharmacie_list  = [p for p in pharmacie]
            #print(pharmacie_list)
            
        parcourt += 1


    ########## Alternance Garde Commune 5 ##########

    tour_com5 = TourGardeCom5.objects.values_list()

    # Convertir le QuerySet en List de tuple
    liste_de_tuple = [t for t in tour_com5]
    #print(liste_de_tuple)

    # Compter le nombre de ligne dans la table
    nombre_tour = TourGarde.objects.all().count()

    parcourt1 = 0
    while parcourt1 < nombre_tour:

        # Parcourir la liste tuple par tuple
        un_tuple = liste_de_tuple[parcourt1]
       
        #print(un_tuple)

        # Convertir le tuple en List
        une_liste = [d for d in un_tuple]
        #print(une_liste)

        # Récuperer les elements de la liste à travers leur indice
        debut_tour = une_liste[1]
        #print(debut_tour)

        fin_tour = une_liste[2]
        #print(fin_tour)

        groupe = une_liste[3]
        #print(groupe)
       
        if date.today() >= debut_tour and date.today() < fin_tour:
            as_debut_tour = debut_tour
            as_fin_tour = fin_tour
            pharmacie = PharmacieGarde.objects.filter(groupe=groupe).values_list('pharmacie', flat=True)
            pharmacie_list_com5  = [p for p in pharmacie]
            #print(pharmacie_list)
            
        parcourt1 += 1


    context = {'date_debut_tour': as_debut_tour, 
               'date_fin_tour': as_fin_tour, 
                'pharmacie_garde': pharmacie_list,
                'pharmacie_garde_com5': pharmacie_list_com5}
    return render(request, 'pharma/liste_pharmacie_garde_today.html', context)

def initialiser_stock(request):
    form = StockForm
    
    if request.method == 'POST':
        form = StockForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/list_stock/')
                     
    context = {'form': form}
    return render(request, 'pharma/initialiser_stock_form.html', context)

def mettre_a_jour_stock(request, pk):
    un_stock = Stock.objects.values_list().filter(id=pk)

    # Convertion de la requete qui est un tuple en liste
    liste_du_stock = [qs for qs in un_stock]
    # print(liste_du_stock)

    # recuperer le premier tuple de la liste
    stock_tuple = liste_du_stock[0]
    # print(stock_tuple)

    # Convertir le premier tuple de la liste en liste
    liste_stock_tuple = [ls for ls in stock_tuple]
    # print(liste_stock_tuple)

    # Recuperer les éléments dans la liste

    """ Pourquoi faire 4 lignes pour recuperer la pharmacie, le produit et l'unité: 
     parce que ces champ dans la table stock sont des clées etrangères, ce qui 
      veut dire que nous avons leur Id et non les données réelles. Donc nous 
       avons utilisé ces Id pour recuperer les données réelles dans leur table
         d'origine.  """
    
    id_pharmacie = liste_stock_tuple[1]
    queryset_pharmacie = PharmacieGarde.objects.filter(id=id_pharmacie)
    liste_pharmacie = [lp for lp in queryset_pharmacie]
    pharmacie = liste_pharmacie[0]

    id_produit = liste_stock_tuple[2]
    queryset_produit = Produit.objects.filter(id=id_produit)
    liste_produit = [lp for lp in queryset_produit]
    produit = liste_produit[0]

    qte_stock = liste_stock_tuple[3]

    id_unite = liste_stock_tuple[4]
    queryset_unite = Unite.objects.filter(id=id_unite)
    liste_unite = [lu for lu in queryset_unite]
    unite = liste_unite[0] 

    if request.method == 'POST':
        nouveau_stock = request.POST['nouveau_stock']
        nouveau_stock = int(nouveau_stock)
        # print(nouveau_stock)

        if nouveau_stock <= 0:
            messages.info(request, "Veuillez saisir un chiffre valide !!!")
            context = {'pharmacie': pharmacie, 'produit': produit, 'unite': unite}
            return render(request, 'pharma/mettre_a_jour_stock_form.html', context)

        qte_stock += nouveau_stock
        # print(qte_stock)

        Stock.objects.update(quantite_stock = qte_stock)

        return redirect('/list_stock/')
    
    context = {'pharmacie': pharmacie, 'produit': produit, 'unite': unite}
    return render(request, 'pharma/mettre_a_jour_stock_form.html', context)

def list_stock(request):
    stocks = Stock.objects.all()
    stockFilter = StockFilter(request.GET, queryset=stocks)
    stock = stockFilter.qs
    context = {"stock": stock, 'stockFilter': stockFilter}
    return render(request, 'pharma/list_stock.html', context)

def ajouter_au_panier(request, pk):
    un_stock = Stock.objects.values_list().filter(id=pk)
    liste_du_stock = [qs for qs in un_stock]
    stock_tuple = liste_du_stock[0]
    liste_stock_tuple = [ls for ls in stock_tuple]

    id_pharmacie = liste_stock_tuple[1]
    queryset_pharmacie = PharmacieGarde.objects.filter(id=id_pharmacie)
    liste_pharmacie = [lp for lp in queryset_pharmacie]
    pharmacie = liste_pharmacie[0]

    print(pharmacie)

    id_produit = liste_stock_tuple[2]
    queryset_produit = Produit.objects.filter(id=id_produit)
    liste_produit = [lp for lp in queryset_produit]
    produit = liste_produit[0]

    print(produit)

    qte_stock = liste_stock_tuple[3]

    qte_produit = 0

    if qte_stock > 0:
        qte_produit += 1 
        
    qte_stock -= qte_produit

    print(qte_produit)

    id_unite = liste_stock_tuple[4]
    queryset_unite = Unite.objects.filter(id=id_unite)
    liste_unite = [lu for lu in queryset_unite]
    unite = liste_unite[0]

    print(unite)

    ordre_vente, created = OrdreVente.objects.get_or_create(id=pk,
                                    pharmacie_ordre=pharmacie,
                                    produit_ordre=produit,
                                    quantite_produit=qte_produit,
                                    unite_ordre=unite)
    if ordre_vente.id == pk:
        ordre_vente.quantite_produit = (ordre_vente.quantite_produit + 1)

    if ordre_vente.quantite_produit < qte_stock:
        messages.info(request, "Stock Epuisé !!!")
        stocks = Stock.objects.all()
        stockFilter = StockFilter(request.GET, queryset=stocks)
        stock = stockFilter.qs
        context = {"stock": stock, 'stockFilter': stockFilter}
        return render(request, 'pharma/list_stock.html', context)
        
    ordre_vente.save()

    return redirect('/list_stock/')

def panier(request):
    ordre_vente = OrdreVente.objects.all()
    context = {'ordre_vente': ordre_vente}
    return render(request, 'pharma/panier.html', context)
