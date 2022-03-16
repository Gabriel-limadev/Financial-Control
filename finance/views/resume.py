from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Sum

from ..models import Revenue, Expense
from ..serializer import RevenueSerializer, ExpenseSerializer


# List a summary in a given month
class ResumeMonth(APIView):
    """Listing summary of given month"""
    def get(self, request, year, month ):
        total_expenses = Expense.objects.filter(date__year=year, date__month=month).aggregate(Sum('value'))['value__sum']
        total_revenues = Revenue.objects.filter(date__year=year, date__month=month).aggregate(Sum('value'))['value__sum']
        expense_for_categorie = Expense.objects.filter(date__year=year,
                                                                date__month=month).values('categorie').annotate(Sum('value'))   

        # Replace value__sum field in each expense with value only
        for expense in expense_for_categorie:
            expense['value'] = expense['value__sum']
            del expense['value__sum']

        final_balance = 0
        if total_expenses and total_revenues:
            final_balance = int(total_expenses) - int(total_revenues)

        # Returning an answer via Json
        return Response({
            'total_expenses': total_expenses,
            'total_revenues': total_revenues,
            'final_balance': final_balance,
            'expense_for_categorie': expense_for_categorie
        })