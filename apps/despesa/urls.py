from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from despesa import views

urlpatterns = [
    path('despesas/', views.DespesaList.as_view()),
    path('despesas/<int:pk>/', views.DespesaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)