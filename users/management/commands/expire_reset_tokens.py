from django.core.management import BaseCommand
from users.models import ResetToken
from django.db import transaction

class Command(BaseCommand):
    help = "Desativar tokens de redefinição de senha expirados"

    def handle(self, *args, **kwargs):
        for token in ResetToken.objects.filter(active=True):

            with transaction.atomic():
                if token.is_expired():
                    token.desactive()