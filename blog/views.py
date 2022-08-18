from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, Type
from .permissions import ReadOnly
from . import models as model


class StandardResultsSetPagination(PageNumberPagination):    
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class HomeBlogView(generics.GenericAPIView):
    
    permission_classes = [IsAuthenticated | ReadOnly]
    serializer_class = PostSerializer
    queryset = model.PostObject.objects.all()
    pagination_class = StandardResultsSetPagination

    def get(self, request):        
        
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        
        if request.user.is_authenticated :

            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid():            
                serializer.create(serializer.data)
                
                return Response({"success":True, "data":serializer.data}, status = status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"success": False, "message":"Unauthenticated"}, status=status.HTTP_403_FORBIDDEN)

