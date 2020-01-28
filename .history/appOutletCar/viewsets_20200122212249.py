from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
@user_passes_test(lambda u: u.is_superuser)
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer