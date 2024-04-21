from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.repositories.infraccion_repository import InfraccionRepository


class InfraccionAV(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return InfraccionRepository.getAll()
    
    def post(self,request):
        return InfraccionRepository.save(request)

class InfraccionDetailAV(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        return InfraccionRepository.findById(pk)
    
    def put(self,request,pk):
        return InfraccionRepository.update(request,pk)
    
    def delete(self,request,pk):
        return InfraccionRepository.destroy(pk)