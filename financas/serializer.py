from rest_framework import serializers
from .models import Categoria, Despesa, Receita
from rest_framework.validators import UniqueForMonthValidator

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    
class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
    
    def validate(self, attrs):
        """Descrição deve ser unica no mesmo mes e ano já existente"""
        if Despesa.objects.filter(descricao=attrs['descricao'], data=attrs['data']).exists():
            raise serializers.ValidationError('Despesa já cadastrada nesse mês')
        return attrs


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
    
    def validate(self, attrs):
        """Descrição deve ser unica no mesmo mes e ano já existente"""
        if Receita.objects.filter(descricao=attrs['descricao'], data=attrs['data']).exists():
            raise serializers.ValidationError('Receita já cadastrada nesse mês')
        return attrs
