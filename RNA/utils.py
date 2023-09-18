from django.contrib.auth.models import Group

def is_member_of_group(user):
    group_name = 'Groupe_autorisé' 
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False
