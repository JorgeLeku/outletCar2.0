from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
from django.contrib.auth.decorators import login_required

@login_required()
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer