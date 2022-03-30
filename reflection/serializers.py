from rest_framework import serializers
from .models import ReflectionEntry
 
# Create a class
class ReflectionEntrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ReflectionEntry
        fields = '__all__'