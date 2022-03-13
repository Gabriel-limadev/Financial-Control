from rest_framework import serializers
from .models import Expense, Revenue

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
    
    def validate(self, data):
        """Description must be unique in the same month and year as existing"""
        if Expense.objects.filter(description=data['description'], date=data['date']).exists():
            print('teste')
            raise serializers.ValidationError({'description':'Expense already registered in this month'})
        return data


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'
    
    def validate(self, data):
        """Description must be unique in the same month and year as existing"""
        if Revenue.objects.filter(description=data['description'], date=data['date']).exists():
            raise serializers.ValidationError({'description':'Revenue already registered in this month'})
        return data
    