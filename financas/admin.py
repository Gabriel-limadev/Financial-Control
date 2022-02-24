from django.contrib import admin
from .models import Categoria, Despesa, Receita
# Register your models here.

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Categoria, Categorias) 

class Despesas(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data')
    list_display_links = ('descricao', 'valor')
    search_fields = ('data',) # Procurar por mes
    list_per_page = 10
    date_hierarchy = 'data'

admin.site.register(Despesa, Despesas)

class Receitas(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data')
    list_display_links = ('descricao', 'valor')
    search_fields = ('data',)
    list_per_page = 10
    date_hierarchy = 'data'

admin.site.register(Receita, Receitas)