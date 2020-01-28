from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
from django.contrib.auth.decorators import admin_requiered

class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer