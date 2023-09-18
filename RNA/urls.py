
from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import tableau
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view,name='home'),
    path('contact/', views.contact_view,name='contact'),
    path('RNA/',include('Redoublement.urls'),name='RNA'),
    path('formulaire/', views.formulaire_view, name='formulaire'),
    # path('confirmation/', views.page_de_confirmation, name='confirmation'),
    path('tableau/', views.tableau_view, name='tableau'),
    path('page-de-restriction/', views.page_restriction, name='page_restriction'),
    path('stat/', views.stat_view, name='stat'),
    path('profession/', views.profession_view, name='profession'),
    path('sexe/', views.sexe_view, name='sexe'),
    path('bac/', views.bac_view, name='bac'),
    path('boursier/', views.boursier_view, name='boursier'),
    path('ville/', views.ville_view, name='ville'),
    path('oui_si/', views.oui_si_view, name='oui_si'),
    path('regime/', views.regime_view, name='regime'),
    path('diplome/', views.diplome_view, name='diplome'),
    path('nationalite/', views.nationalite_view, name='nationalite'),
    path('Mention/', views.mention_view, name='Mention'),
    path('login/', views.login_view, name='login'),
    
]
