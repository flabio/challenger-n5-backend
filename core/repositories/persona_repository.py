from rest_framework.response import Response
from rest_framework import status
from core.domain.persona.models import Persona
from core.serializers.persona_serializer import PersonaSerializer


class PersonaRepository:
    
    def getAll():
        try:
            queryset=Persona.objects.all()
            serializer=PersonaSerializer(queryset,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({'error':'error query'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def findById(pk):
        try:
            queryset=Persona.objects.get(pk=pk)
            serializer=PersonaSerializer(queryset)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({'error':'No existe el id.'},status=status.HTTP_400_BAD_REQUEST)
    
    def getfindByEmial(email):
        try:
            queryset=Persona.objects.get(email=email)
            serializer=PersonaSerializer(queryset)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({'error':'No existe el email.'},status=status.HTTP_400_BAD_REQUEST)
        
        
    def getValidateByFindByEmail(email):
        return Persona.objects.filter(email=email)
    
    def save(request):
        try:
            serializer = PersonaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'se guardo correctamente','data':serializer.data},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Persona.DoesNotExist:
            return Response({'error':'error query'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(request,pk):
        try:
            queryset=Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            return Response({'error':'no se existe el id'},status=status.HTTP_404_NOT_FOUND)
   
        serializer = PersonaSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'se actualozo correctamente','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(pk):
        try:
            queryset=Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            return Response({'error':'no se existe el id'},status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({'message':'se elimino correctamente'},status=status.HTTP_200_OK)