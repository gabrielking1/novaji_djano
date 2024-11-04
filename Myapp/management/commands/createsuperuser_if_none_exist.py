from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a superuser if none exist'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                'admin@example.com',
                'adminpassword',
              
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
