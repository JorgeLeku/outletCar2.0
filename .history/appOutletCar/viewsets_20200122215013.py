from rest_framework import viewsets
from .models import Coche
from .serializer import CocheSerializer
const { AbilityBuilder } = require('casl');
class CocheViewSet(viewsets.ModelViewSet):
    if (abilities.can('update', 'Post')) {
  
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer

}