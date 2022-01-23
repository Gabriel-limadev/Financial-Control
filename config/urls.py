from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.despesa.urls')),
    path('', include('apps.receita.urls'))
]
