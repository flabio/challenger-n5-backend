from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from core.repositories.vehiculo_repository import VehiculoRepository




class VehiculoAv(APIView):
    
    def get(self, request):
        return VehiculoRepository.getAll()
    def post(self,request):
        
        if len(request.data.get('placa'))==0:
            return Response({'message':'la placa es requerida'},status=status.HTTP_400_BAD_REQUEST)
        
        if len(request.data.get('marca'))==0:
            return Response({'message':'la marca es requerida'},status=status.HTTP_400_BAD_REQUEST)
        
        exist_placa=VehiculoRepository.existPlaca(request.data.get('placa'))
        
        if exist_placa.exists():
            return Response({'message':'la placa ya existe'},status=status.HTTP_400_BAD_REQUEST)
        
        
        return VehiculoRepository.save(request)

class VehiculoDetailAv(APIView):
    
    def get(self,request,pk):
        return VehiculoRepository.findById(pk)
     
    def put(self,request,pk):
        return VehiculoRepository.update(request,pk)
        
    def delete(self,request,pk):
        return VehiculoRepository.destroy(pk)
        
    