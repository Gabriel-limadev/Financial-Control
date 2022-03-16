from rest_framework import filters, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Sum

from ..models import Expense
from ..serializer import ExpenseSerializer

# Customizing an expense search query
class ExpenseList(APIView):
    """Showing all expenses"""
    def get(self, request, format=None):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Searches
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']


class ExpenseDetail(APIView):
    """
    Retrieve, update or delete a expense instance.
    """
    def get_object(self, pk):
        try: 
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        expense = self.get_object(pk)
        expense.delete()
        return Response({'message': 'Expense successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
    

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