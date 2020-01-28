from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer

class CocheViewSet(viewsets.ModelViewSet):
     if not request.user.is_superuser:
         return HttpResponse(status=403)
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer