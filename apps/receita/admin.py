from django.contrib import admin
from receita.models import Receita


class receita(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', )
    
admin.site.register(Receita, receita)