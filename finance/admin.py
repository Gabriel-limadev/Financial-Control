from django.contrib import admin
from .models import Expense, Revenue
# Register your models here.

class Expenses(admin.ModelAdmin):
    list_display = ('description', 'value', 'date')
    list_display_links = ('description', 'value')
    search_fields = ('date',) # Procurar por mes
    ordering = ['description']
    list_per_page = 10
    date_hierarchy = 'date'

admin.site.register(Expense, Expenses)

class Revenues(admin.ModelAdmin):
    list_display = ('description', 'value', 'date')
    list_display_links = ('description', 'value')
    search_fields = ('date',)
    ordering = ['description']
    list_per_page = 10
    date_hierarchy = 'date'

admin.site.register(Revenue, Revenues)