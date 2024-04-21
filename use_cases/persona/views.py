from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.repositories.persona_repository import PersonaRepository

# Create your views here.
class PersonaAv(APIView):
    
    def get(self,request):
        return PersonaRepository.getAll()
    
    def post(self, request):
        
        if len(request.data.get('name'))==0:
            return Response({'message':'the name is required.'},status=status.HTTP_400_BAD_REQUEST)
        
        if len(request.data.get('email'))==0:
            return Response({'message':'the email is required.'},status=status.HTTP_400_BAD_REQUEST)
        
        if PersonaRepository.getValidateByFindByEmail(request.data.get('email')):
            return Response({'message':'the email ready.'},status=status.HTTP_400_BAD_REQUEST)
         
        return PersonaRepository.save(request)
        
class PersonaDetalleAv(APIView):
    
    def get(self,request,pk):
        return PersonaRepository.findById(pk)
        
    def put(self,request,pk):
        return PersonaRepository.update(request,pk)
    
    def delete(self,request,pk):
        return PersonaRepository.destroy(pk)
    
class PersonaInformeDetail(APIView):
    
    def get(self,request,email ):
        return PersonaRepository.getfindByEmial(email)
        
    

