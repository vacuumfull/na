from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from message.models import Message


class Command(BaseCommand):

	help = 'our help string comes here'

	def _init_messages(self):
		user = User.objects.get(pk=1)
		Message.objects.create(content='Hello', from_user=user, to_user=user, dialog_id=1)
	
	def handle(self, *args, **options):
		self._init_messages()