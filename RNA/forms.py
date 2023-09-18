from django import forms
from Redoublement.models import Etudiant

from django.contrib.auth.forms import AuthenticationForm

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant  
        fields = ['Nationalité', 'Filière', 'Identifiant', 'Age_bac']  



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Identifiant',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label='Mot de passe',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )