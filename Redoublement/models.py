from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class Etudiant(models.Model):
    Nationalité=models.CharField(max_length=64)
    Filière=models.CharField(max_length=64)
    Identifiant=models.IntegerField()
    Age_bac=models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.Nationalité} en {self.Filière} identifiant cd {self.Identifiant}, agé de {self.Age_bac} ans au bac" 
    


group, created = Group.objects.get_or_create(name='nom_de_votre_groupe')




class FormulairePermission(models.Model):
    class Meta:
        permissions = [
            ("can_view_formulaire", "Can view Formulaire page"),
        ]


# from django.contrib.auth.models import Permission
# content_type = ContentType.objects.get_for_model('contact.html')
# # Créez une permission personnalisée pour accéder à la page de contact
# permission = Permission.objects.create(
#     codename='can_access_contact',
#     name='Can Access Contact Page',
#     content_type=content_type,
# )
