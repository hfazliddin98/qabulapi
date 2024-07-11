from rest_framework.viewsets import ModelViewSet
from .models import Ariza, Qolanma
from .serialazer import QolanmaSerializer, ArizaSerializer


class ArizaViewSet(ModelViewSet):
    queryset = Ariza.objects.all()
    serializer_class = ArizaSerializer

class QolanmaViewSet(ModelViewSet):
    queryset = Qolanma.objects.all()
    serializer_class = QolanmaSerializer