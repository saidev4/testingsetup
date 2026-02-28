from django.shortcuts import render

from rest_framework.views import APIView
from .models import students 
from .serializers import StudentSerializer 
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.


class StudentView(APIView):
    def get(self,request):
        student = students.objects.all()
        serializer = StudentSerializer(student ,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.isvalid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error)
