from django.contrib import admin
from .models import DataTable
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']

admin.site.register(DataTable, Admin)