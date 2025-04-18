from rest_framework import serializers
from .models import *

class StudentSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class EventSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class CommentsSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        
class LikeSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'