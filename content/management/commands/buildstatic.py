import os, subprocess
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Generar static_build/ y push a main"

    def handle(self, *args, **options):
        # collectstatic
        call_command('collectstatic', '--noinput', verbosity=0)
        # export distill
        call_command('distill-local', '--output-dir', 'static_build')
        # git subtree push
        subprocess.check_call([
            'git','subtree','push',
            '--prefix','static_build',
            'origin','main'
        ])
        self.stdout.write(self.style.SUCCESS("✅ Static site en main"))
