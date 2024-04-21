from rest_framework.response import Response
from rest_framework import status
from core.domain.vehiculo.models import Vehiculo
from core.serializers.vehiculo_serializer import VehiculoSerializer



class VehiculoRepository:
    
    def getAll():
        try:
            queryset=Vehiculo.objects.all()
            serializer=VehiculoSerializer(queryset,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Vehiculo.DoesNotExist:
            return Response({'error':'error query'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def findById(pk):
        try:
            queryset=Vehiculo.objects.get(pk=pk)
            serializer=VehiculoSerializer(queryset)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Vehiculo.DoesNotExist:
            return Response({'error':'No existe el id'},status=status.HTTP_400_BAD_REQUEST)
    
    def existPlaca(placa):
        return Vehiculo.objects.filter(placa=placa) 
    
    def save(request):
        try:
            serializer = VehiculoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'se guardo correctamente','data':serializer.data},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Vehiculo.DoesNotExist:
            return Response({'error':'error query'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(request,pk):
        try:
            queryset=Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response({'error':'no se existe el id'},status=status.HTTP_404_NOT_FOUND)
   
        serializer = VehiculoSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'se actualozo correctamente','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(pk):
        try:
            queryset=Vehiculo.objects.get(pk=pk)
        except Vehiculo.DoesNotExist:
            return Response({'error':'no se existe el id'},status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({'message':'se elimino correctamente'},status=status.HTTP_200_OK)