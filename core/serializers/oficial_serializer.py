from rest_framework import serializers

from core.domain.oficial.models import Account

class OficialSerializer(serializers.ModelSerializer):
        password2= serializers.CharField(style={'input_type':'password'},write_only=True)
        class Meta:
            model = Account
            fields=['email','password','password2','first_name','last_name','number_identification']
            extra_kwargs={
                'password':{'write_only':True}
            }
        def save(self):
            password=self.validated_data['password']
            password2=self.validated_data['password2']
            
            if password!=password2:
                raise serializers.ValidationError({'error':'El password de confirmacion no  coincide'})
            
            if Account.objects.filter(email=self.validated_data['email']).exists():
                raise serializers.ValidationError({'error':'El email del usuario ya existe'})
            
            account = Account.objects.create_user(
                first_name  =   self.validated_data['first_name'],
                last_name   =   self.validated_data['last_name'],
                email       =   self.validated_data['email'],
                password    =   self.validated_data['password'],
                number_identification=self.validated_data['number_identification']
            )
            account.set_password=self.validated_data['password']
            
            account.save()
            return account