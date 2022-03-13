from rest_framework import viewsets, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .models import Expense, Revenue
from .serializer import ExpenseSerializer, RevenueSerializer
from rest_framework.permissions import IsAuthenticated

# Customizing an expense search query
class ExpensesViewSet(viewsets.ModelViewSet):
    """showing all expenses"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # Searches
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
    # Authentication
    permission_classes = [IsAuthenticated]


# Customizing a revenue search query
class RevenuesViewSet(viewsets.ModelViewSet):
    """showing all revenues"""
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    # Searches
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
    # Authentication
    permission_classes = [IsAuthenticated]


# List revenue in a given month
class RevenuesMonth(generics.ListAPIView):
    """Listing all revenues in a month"""
    def get_queryset(self):
        queryset = Revenue.objects.filter(date__year=self.kwargs['year'], date__month=self.kwargs['month'])
        return queryset
    serializer_class = RevenueSerializer
    # Searches
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
    # Authentication
    permission_classes = [IsAuthenticated]


# List expense in a given month
class ExpensesMonth(generics.ListAPIView):
    """Listing all expenses in a month"""
    def get_queryset(self):
        queryset = Expense.objects.filter(date__year=self.kwargs['year'], date__month=self.kwargs['month'])
        return queryset
    serializer_class = ExpenseSerializer
    # Buscas
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
    # Authentication
    permission_classes = [IsAuthenticated]


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