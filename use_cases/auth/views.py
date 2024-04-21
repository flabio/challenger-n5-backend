from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.repositories.auth_repository import AuthRepository

@api_view(['POST',])
def logout_view(request):
    if request.method=='POST':
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST',])
def login_view(request):
    return AuthRepository.login(request)

@api_view(['GET',])
def oficial_all_view(request):
    return AuthRepository.getAll()