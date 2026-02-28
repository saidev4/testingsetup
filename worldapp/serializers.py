from .models import students
from rest_framework import serializers 

class StudentSerializer(serializers.ModelSerializer):
    class Meta :
        model = students 
        fields =  "__all__"