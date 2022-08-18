from rest_framework import serializers
from .models import CoreUser

class CoreUserSerializer(serializers.Serializer):

    email = serializers.EmailField()    
    password = serializers.CharField(max_length=100, write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)    
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = CoreUser
        fields = ['email', 'password',  'first_name', 'last_name','groups']

    def create(self, validated_data):
        user = CoreUser.objects.create_user(**validated_data)
        user.save()
        return user