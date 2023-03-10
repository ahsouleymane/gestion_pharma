from django.urls import path, include
from pharma import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('ajouter_pharmacie/', views.ajouter_pharmacie, name='ajouter_pharmacie'),
    path('editer_pharmacie/<int:pk>/', views.editer_pharmacie, name='editer_pharmacie'),
    path('supprimer_pharmacie/<int:pk>/', views.supprimer_pharmacie, name='supprimer_pharmacie'),
    path('ajouter_stock/', views.ajouter_stock, name='ajouter_stock'),
    path('mettre_a_jour_stock/<int:pk>/', views.mettre_a_jour_stock, name='mettre_a_jour_stock'),
    path('rechercher_produit_en_fonction_de_pharmacie_et_stock/<int:pk>/', 
         views.rechercher_produit_en_fonction_de_pharmacie_et_stock, name='rechercher_produit_en_fonction_de_pharmacie_et_stock'),
]