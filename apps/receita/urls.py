from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from receita import views

urlpatterns = [
    path('receitas/', views.ReceitaList.as_view()),
    path('receitas/<int:pk>/', views.ReceitaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
