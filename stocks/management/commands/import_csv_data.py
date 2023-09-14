from django.core.management.base import BaseCommand
from stocks.models import DataTable
from stocks.models import importFromCSV

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **kwargs):
        importFromCSV()
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))