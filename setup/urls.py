from django.contrib import admin
from django.urls import path, include
from financas.views import DepesasViewSet, ReceitasViewSet, CategoriasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categorias', CategoriasViewSet, basename='Categorias')
router.register('despesas', DepesasViewSet, basename='Despesas')
router.register('receitas', ReceitasViewSet, basename='Receitas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
