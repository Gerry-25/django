from django.contrib import admin
from django.urls import path, include

from . import views
from Redoublement.views import tableau

urlpatterns = [
    
    path('',views.article_view,name='RNA'),
    path('tableau/', tableau, name='tableau'),
    path('ajouter-donnees/', views.ajouter_donnees, name='ajouter_donnees'),
    
]

