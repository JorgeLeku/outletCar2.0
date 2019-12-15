from rest_framework import viewsets
class CocheViewSet(viewsets.ModelViewSet):
    queryset = Coche.objects.all()
    serializers_class = CocheSerializer