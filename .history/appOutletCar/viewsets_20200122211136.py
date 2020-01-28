from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer

@has_add_permission()
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer