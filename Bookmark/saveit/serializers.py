from rest_framework import serializers
from rest_framework import serializers
from .models import Bookmark
from django.utils import timezone

class Bookmark_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    url = serializers.CharField(max_length=100)
    
    def create(self,validate_data):
        return Bookmark.objects.create(**validate_data)


