from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
from django.contrib.auth.decorators import has_delete_permission()

class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer