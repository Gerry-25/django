import pandas as pd
from django.contrib.auth.models import User,Group
group, created = Group.objects.get_or_create(name='Groupe_autorisé')
#Fichier excel avec noms des personnes autorisées
df = pd.read_excel('Restreint.xlsx')

# Parcours des lignes du DataFrame pour ajouter les utilisateurs au groupe
for index, row in df.iterrows():
    username = row['Nom_utilisateur']
    user = User.objects.get(username=username)
    user.groups.add(group)


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import Permission

# Créez une permission personnalisée pour accéder à la page de contact
permission, created = Permission.objects.get_or_create(
    codename='can_access_contact',
    name='Can Access Contact Page',
)

from django.contrib.auth.models import Group

# Obtenez le groupe "Administration" (ou créez-le si nécessaire)
group, created = Group.objects.get_or_create(name='Administration')

# Ajoutez la permission à ce groupe
group.permissions.add(permission)

