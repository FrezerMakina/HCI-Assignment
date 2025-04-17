from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views here.
class StudentViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentSerilializer
    
    def list(self, request):
        queryset = Student.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
