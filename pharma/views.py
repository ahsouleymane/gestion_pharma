from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def ajouter_stock(request):
    pass

def mettre_a_jour_stock(request):
    pass

def rechercher_produit_en_fonction_de_pharmacie_et_stock(request):
    pass

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

    
    number_of_location = Pharmacie.objects.all().count()
    #print('Number of location: ', number_of_location)

    locations = []

    parcourt = 0
    while parcourt < number_of_location:

        locations = Pharmacie.objects.values_list('designation', flat=True)
        parcourt += 1

    #print(locations)


    latitudes = []
    longitudes = []

    parcourt = 0
    while parcourt < number_of_location:

        latitudes = Pharmacie.objects.values_list('latitude', flat=True)
        longitudes = Pharmacie.objects.values_list('longitude', flat=True)

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

    m = folium.Map(width=1600, height=600, location=get_center_coordinates(x_lat, x_lon), zoom_start=12)

    # Location marker
    folium.Marker([x_lat, x_lon], tooltip='click here for more', popup=city['city'], 
                    icon=folium.Icon(color='purple')).add_to(m)
    
    pharmacies = Pharmacie.objects.all()

    for pharmacie in pharmacies:
        coordinates = (pharmacie.latitude, pharmacie.longitude)
        folium.Marker(coordinates, popup=pharmacie.designation,
                      tooltip='Cliquer ici pour afficher le nom de la pharmacie', 
                      icon=folium.Icon(color='red')).add_to(m)

    # Get HTML representation of map object
    m = m._repr_html_()

    context = {'map': m, 'distances': distances}
    return render(request, 'pharma/afficher_distance_pharmacie.html', context)

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

