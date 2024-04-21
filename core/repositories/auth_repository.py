from django.contrib import auth

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from core.domain.oficial.models import Account
from core.serializers.oficial_serializer import OficialSerializer


class AuthRepository:
    
    def login(request):
        data={}
        if request.method=='POST':
            email=request.data.get('email')
            
            password=request.data.get('password')
            account=auth.authenticate(email=email,password=password)
    
            
            if account is not None:
                data['response']='El login fue exitoso'
                data['username']=account.username
                data['email']=account.email
                data['first_name']=account.first_name
                data['last_name']=account.last_name
                data['number_identification']=account.number_identification
                refresh= RefreshToken.for_user(account)
                data['token']={
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }
                return Response(data)
            else:
                data['error']='Credeciales incorrectas'
                return Response(data,status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def getAll():
        try:
            queryset=Account.objects.all()
            serializer=OficialSerializer(queryset,many=True)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
               
        except Account.DoesNotExist:
            return Response({'error':''},status=status.HTTP_400_BAD_REQUEST)
    
    def save(request):
        try:
            if request.method=='POST':
                serializer=OficialSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message':'se guardo correctamente','data':serializer.data},status=status.HTTP_201_CREATED)
                else:
                    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
               
        except Account.DoesNotExist:
            return Response({'error':''},status=status.HTTP_400_BAD_REQUEST)
    