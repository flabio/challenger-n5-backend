from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.repositories.auth_repository import AuthRepository


# Create your views here.
class OficialAv(APIView):
    
    def get(self,request):
        return AuthRepository.getAll()
    
    def post(self, request):
        
        return AuthRepository.save(request)
        
# class PersonaDetalleAv(APIView):
    
#     def get(self,request,pk):
#         return PersonaRepository.findById(pk)
        
#     def put(self,request,pk):
#         return PersonaRepository.update(request,pk)
    
#     def delete(self,request,pk):
#         return PersonaRepository.destroy(pk)
    
# class PersonaInformeDetail(APIView):
    
#     def get(self,request,email ):
#         return PersonaRepository.getfindByEmial(email)
        
    