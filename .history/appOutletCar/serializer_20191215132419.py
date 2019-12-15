from rest_framework import serializers
from .models import Coche
class cocheSerializer(serializers.ModelSerializer):
    class class Meta:
        model = Coche