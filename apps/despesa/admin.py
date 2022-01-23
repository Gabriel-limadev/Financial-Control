from django.contrib import admin
from despesa.models import Despesa

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', )
    
admin.site.register(Despesa, Despesas)
