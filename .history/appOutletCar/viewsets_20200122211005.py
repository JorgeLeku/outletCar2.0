from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer

@admin_requiered
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer