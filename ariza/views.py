from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Ariza, Qolanma
from .serializer import QolanmaSerializer, ArizaSerializer



class ArizaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Ariza.objects.all()
    serializer_class = ArizaSerializer

class QolanmaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Qolanma.objects.all()
    serializer_class = QolanmaSerializer

