from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):

    help = 'our help string comes here'

    def _create_groups(self):
        
        users = Group(name='Пользователи')
        users.save()
        users.permissions.set([37, 38, 39, 52, 53, 54, 49, 50, 51, 58, 60, 61, 62, 63])
       
        musicains = Group(name='Музыканты')
        musicains.save()
        musicains.permissions.set([37, 38, 39, 52, 53, 54, 49, 50, 51, 58, 60, 61, 62, 63, 25, 26, 27])

        deputies = Group(name='Представители')
        deputies.save()
        deputies.permissions.set([37, 38, 39, 52, 53, 54, 49, 50, 51, 58, 60, 61, 62, 63, 25, 26, 27, 31, 32, 33])
       
        organizers = Group(name='Организаторы')
        organizers.save()
        organizers.permissions.set([37, 38, 39, 52, 53, 54, 49, 50, 51, 58, 60, 61, 62, 63, 31, 32, 33, 34, 35, 36])
       

    def handle(self, *args, **options):
        self._create_groups()
