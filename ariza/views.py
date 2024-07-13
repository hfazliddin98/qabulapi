from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Ariza, Qolanma
from .serialazer import QolanmaSerializer, ArizaSerializer


class ArizaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Ariza.objects.all()
    serializer_class = ArizaSerializer

class QolanmaViewSet(ModelViewSet):
    queryset = Qolanma.objects.all()
    serializer_class = QolanmaSerializer