from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from .utils import is_member_of_group
from django.contrib.auth.decorators import login_required
from Redoublement.models import Etudiant
from .forms import EtudiantForm
from django.contrib.auth.forms import UserCreationForm
#from authentication.models import User

from django.contrib.auth.models import Permission
# >>> permission = Permission.objects.get(codename='add_photo')
# >>> user.user_permissions.add(permission)
# >>> user = User.objects.get(username='toto')

@login_required(login_url='/login/')  
def contact_view(request):
    if request.user.has_perm('yourapp.can_access_contact'):
        return render(request, 'contact.html')
    else:
        return("cant access")

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and is_member_of_group(user):
                login(request, user)
                return redirect('contact.html')
            else:
                messages.error(request, "Identifiants invalides ou vous n'avez pas l'autorisation d'accéder à cette page.")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')  
def contact_view(request):
    return render(request, 'contact.html')


def stat_view(request):
    return render(request,'stat.html')

def profession_view(request):
    return render(request,'profession.html')

def sexe_view(request):
    return render(request,'sexe.html')

def bac_view(request):
    return render(request,'bac.html')

def boursier_view(request):
    return render(request,'boursier.html')

def mention_view(request):
    return render(request,'Mention.html')


def ville_view(request):
    return render(request,'ville.html')

def diplome_view(request):
    return render(request,'diplome.html')

def nationalite_view(request):
    return render(request,'nationalite.html')

def regime_view(request):
    return render(request,'regime.html')

def oui_si_view(request):
    return render(request,'oui_si.html')

def formulaire_view(request):
    formulaire_rempli = False
    form = EtudiantForm()  

    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            formulaire_rempli = True


    return render(request, 'formulaire.html', {'form': form, 'formulaire_rempli': formulaire_rempli})

def page_restriction(request):
    return render(request, 'page_restriction.html')


def home_view(request):
    return render(request,'home.html')
    #return HttpResponse('Hello World!')




#def formulaire_view(request):
    #if request.method == 'POST':
        #donnees = request.POST
        #nouvel_objet = Etudiant(Nationalité=donnees['Nationalité'], Filière=donnees['Filière'],Identifiant=donnees['Identifiant'],Age_bac=donnees['Age_bac'])
        #nouvel_objet.save()
        #return redirect('page_de_confirmation')
    #return render(request, 'formulaire.html')



def tableau_view(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'tableau.html', {'etudiants': etudiants})
