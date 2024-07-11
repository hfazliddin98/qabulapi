from rest_framework import serializers
from .models import Ariza, Qolanma

class ArizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariza
        fields = '__all__'


class QolanmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qolanma
        fields = '__all__'