from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        if options['hello']:
            import __hello__
        else:
            import this

    def add_arguments(self, parser):
        parser.add_argument(
            '-hw',
            '--hello',
            action='store_true',
            default=False,
            help='Вывод короткого сообщения'
        )