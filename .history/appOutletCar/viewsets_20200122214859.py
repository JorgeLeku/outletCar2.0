from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer

class CocheViewSet(viewsets.ModelViewSet):
    if (user.type === ADMIN || user.auth && post.owner === user.id ) {
  
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer

}