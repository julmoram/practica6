from django.shortcuts import render
from .serializer import Floreriaserializer, Follajeserializer
from .models import Floreria, Follaje
from rest_framework import viewsets
# Create your views here.
class FloreriaViewset(viewsets.ModelViewSet):
    queryset=Floreria.objects.all()
    serializer_class = Floreriaserializer  #Asociamos el serializador a la clase de vista
    
class FollajeViewset(viewsets.ModelViewSet):
    queryset=Follaje.objects.all()
    serializer_class = Follajeserializer  #Asociamos el serializador a la clase de vista
    
    
