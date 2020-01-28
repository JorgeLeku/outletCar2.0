from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer