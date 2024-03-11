from rest_framework import serializers
from .models import Floreria, Follaje

class Floreriaserializer(serializers.ModelSerializer):
    class Meta:
        model= Floreria
        fields= '__all__'
    
class Follajeserializer(serializers.ModelSerializer):
    class Meta:
        model= Follaje
        fields= '__all__'