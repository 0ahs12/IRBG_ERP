from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.sites.models import Site
from allauth.account.signals import user_signed_up
from .models import CustomUser

@receiver(user_signed_up)
def assign_group(sender, user, request, **kwargs):
    authors_group, created = Group.objects.get_or_create(name='Authors')
    user.groups.add(authors_group)
