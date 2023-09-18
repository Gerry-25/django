from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Etudiant
from django.core.paginator import Paginator
from .db_articles import data
import pandas as pd
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group


def ajouter_donnees(request):
    if request.method == 'POST':
        donnees = request.POST
        nouvel_objet = Etudiant(Nationalité=donnees['Nationalité'], Filière=donnees['Filière'],Identifiant=donnees['Identifiant'],Age_bac=donnees['Age_bac'])
        nouvel_objet.save()
        #return redirect('page_de_confirmation')
    return render(request, 'formulaire.html')  
#def article_view(request):
    
    #context={
        #"data":data
    #}

    #return render(request,'Redoublement/RNA.html',context)

#def article_view(request):
    #data = [
        #{"nom": "John", "age": 25,"sexe":"M"},
        #{"nom": "Alice", "age": 30,"sexe":"F"},
        #{"nom": "Bob", "age": 27,"sexe":"M"},
        #{"nom": "Ines", "age": 24,"sexe":"F"}
    #]
    #context = {
        #"data": data
    #}
    #print(data)  
    #return render(request, 'Redoublement/RNA.html', context)
  

def article_view(request):
    # Chemin vers le fichier Excel
    #chemin_fichier = "C:/Users/pret/Desktop/RNA/RNA/Resultat_licence.xlsx"
    #chemin_fichier="C:/Users/pret/Desktop/RNA/RNA/prediction_licence1.xlsx"
    chemin_fichier="C:/Users/pret/Desktop/RNA/RNA/intersec (1).xlsx"
    
    # Lecture du fichier Excel et création d'un DataFrame
    dataframe = pd.read_excel(chemin_fichier)
    
    # Conversion du DataFrame en liste de dictionnaires
    donnees = dataframe.to_dict(orient='records')
    
    # Initialisation du paginator
    paginator = Paginator(donnees, 50)  # Division en pages de 5 éléments chacune
    
    # numéro de page à partir de la requête GET
    page_number = request.GET.get('page')
    
    # Récupération des éléments de la page actuelle
    donnees_page = paginator.get_page(page_number)
    num_page = donnees_page.number
    previous_page = num_page - 1 if num_page > 1 else None
    next_page = num_page + 1 if num_page < donnees_page.paginator.num_pages else None


    
    # Passage des données paginées au modèle
    context = {
        'donnees': donnees_page,
        'previous_page': previous_page,
        'next_page': next_page,
    }
    return render(request, 'Redoublement/RNA.html', context)

   

def tableau(request):

    return render(request, 'Redoublement/RNA.html',{'data':data})





