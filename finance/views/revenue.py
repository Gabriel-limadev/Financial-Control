from rest_framework import filters, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Sum

from ..models import Revenue
from ..serializer import RevenueSerializer


class RevenueList(APIView):
    """Showing all expenses"""
    def get(self, request, format=None):
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RevenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    # Searches
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']


class RevenueDetail(APIView):
    """
    Retrieve, update or delete a revnue instance.
    """
    def get_object(self, pk):
        try:
            return Revenue.objects.get(pk=pk)
        except Revenue.DoesNotExist:
            raise Http404()
    
    def get(self, request, pk, format=None):
        revenue = self.get_object(pk)
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        revenue = self.get_object(pk)
        serializer = RevenueSerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        revenue = self.get_object(pk)
        revenue.delete()
        return Response({'message' : 'Revenue successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
    

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