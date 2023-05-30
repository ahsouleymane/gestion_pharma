from django.urls import path, include
from pharma import views
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('', views.acceuil, name='acceuil'),

     path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    
     path('ajouter_pharmacie_form/', views.ajouter_pharmacie, name='ajouter_pharmacie_form'),
    
     path('list_pharmacie/', views.list_pharmacie, name='list_pharmacie'),

     path('editer_pharmacie_form/<int:pk>/', views.editer_pharmacie, name='editer_pharmacie_form'),
    
     path('supprimer_pharmacie_form/<int:pk>/', views.supprimer_pharmacie, name='supprimer_pharmacie_form'),
    
     path('list_produit/', views.list_produit, name='list_produit'),

     path('list_pharmacie_garde/', views.liste_pharmacie_garde, name='list_pharmacie_garde'),

     path('editer_pharmacie_garde_live/', views.editer_pharmacie_garde_live, name='editer_pharmacie_garde_live'),

     path('liste_tour_garde/', views.liste_tour_garde, name='liste_tour_garde'),

     path('liste_tour_garde_com5/', views.liste_tour_garde_com5, name='liste_tour_garde_com5'),

     path('liste_pharmacie_garde/', views.liste_pharmacie_garde, name='liste_pharmacie_garde'),
     
     path('ajouter_stock/', views.ajouter_stock, name='ajouter_stock'),
    
     path('mettre_a_jour_stock/<int:pk>/', views.mettre_a_jour_stock, name='mettre_a_jour_stock'),
    
     path('rechercher_produit_en_fonction_de_pharmacie_et_stock/<int:pk>/', 
         views.rechercher_produit_en_fonction_de_pharmacie_et_stock, name='rechercher_produit_en_fonction_de_pharmacie_et_stock'),

     path('localisation_et_calcule_de_distance/', views.localisation_et_calcule_de_distance,
         name='localisation_et_calcule_de_distance'),

     path('mettre_a_jour_stock/', views.mettre_a_jour_stock, name='mettre_a_jour_stock'),

]