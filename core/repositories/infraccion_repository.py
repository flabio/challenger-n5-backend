from rest_framework.response import Response
from rest_framework import status
from core.domain.infraccion.models import Infraccion
from core.serializers.infraccion_serializer import InfraccionCreateSerializer, InfraccionSerializer


class InfraccionRepository:
    
    def getAll():
        try:
            queryset=Infraccion.objects.all()
            serializer=InfraccionSerializer(queryset,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Infraccion.DoesNotExist:
            return Response({'error':'error query'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def findById(pk):
        try:
            queryset=Infraccion.objects.get(pk=pk)
            serializer=InfraccionSerializer(queryset)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Infraccion.DoesNotExist:
            return Response({'error':'No existe el id'},status=status.HTTP_400_BAD_REQUEST)
    
    def save(request):
        try:
            serializer = InfraccionCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'se guardo correctamente','data':serializer.data},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Infraccion.DoesNotExist:
            return Response({'error':'error query'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(request,pk):
        try:
            queryset=Infraccion.objects.get(pk=pk)
        except Infraccion.DoesNotExist:
            return Response({'error':'no se existe el id'},status=status.HTTP_404_NOT_FOUND)
   
        serializer = InfraccionSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'se actualozo correctamente','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(pk):
        try:
            queryset=Infraccion.objects.get(pk=pk)
        except Infraccion.DoesNotExist:
            return Response({'error':'no se existe el id'},status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({'message':'se elimino correctamente'},status=status.HTTP_200_OK)