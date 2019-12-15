from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializers_class = CocheSerializer