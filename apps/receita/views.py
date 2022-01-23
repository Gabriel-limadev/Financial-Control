from receita.models import Receita
from receita.serializer import ReceitaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ReceitaList(APIView):
    
    def get(self, request, format=None):
        receitas = Receita.objects.all()
        serializer = ReceitaSerializer(receitas, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ReceitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReceitaDetail(APIView):

    def get_object(self, pk):
        try:
            return Receita.objects.get(pk=pk)
        except Receita.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        receitas = self.get_object(pk)
        serializer = ReceitaSerializer(despesas)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        receitas= self.get_object(pk)
        serializer = ReceitaSerializer(receitas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        receitas = self.get_object(pk)
        receitas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
