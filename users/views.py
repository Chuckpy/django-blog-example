from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import generics
from rest_framework.settings import api_settings
from .models import CoreUser
from .serializers import CoreUserSerializer


class CoreUserView(generics.GenericAPIView):

    serializer_class = CoreUserSerializer
    permission_class=(AllowAny,)
    queryset = CoreUser.objects.all()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try : 
            user = CoreUser.objects.get(email=serializer.validated_data['email'])
            if user :
                return Response({"success":False, "error":"Already have a user with this email"}, status=status.HTTP_400_BAD_REQUEST )
        except CoreUser.DoesNotExist:            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


