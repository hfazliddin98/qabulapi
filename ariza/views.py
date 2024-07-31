from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Ariza, Qolanma
from .models import BakalavrHujat, BakalavrBolim, BakalavrTolov, BakalavrMalumot
from .models import MagistrHujat, MagistrBolim, MagistrTolov, MagistrMalumot
from .models import PhdHujat, PhdBolim, PhdTolov, PhdMalumot
from .models import DscHujat, DscBolim, DscTolov, DscMalumot
from .serializer import QolanmaSerializer, ArizaSerializer
from .serializer import BakalavrHujatSerializer, BakalavrBolimSerializer, BakalavrTolovSerializer, BakalavrMalumotSerializer
from .serializer import MagistrHujatSerializer, MagistrBolimSerializer, MagistrTolovSerializer, MagistrMalumotSerializer
from .serializer import PhdHujatSerializer, PhdBolimSerializer, PhdTolovSerializer, PhdMalumotSerializer
from .serializer import DscHujatSerializer, DscBolimSerializer, DscTolovSerializer, DscMalumotSerializer


class ArizaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Ariza.objects.all()
    serializer_class = ArizaSerializer

class QolanmaViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Qolanma.objects.all()
    serializer_class = QolanmaSerializer

class BakalavrHujatViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = BakalavrHujat.objects.all()
    serializer_class = BakalavrHujatSerializer

    
class BakalavrBolimViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = BakalavrBolim.objects.all()
    serializer_class = BakalavrBolimSerializer

    
class BakalavrTolovViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = BakalavrTolov.objects.all()
    serializer_class = BakalavrTolovSerializer

    
class BakalavrMalumotViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = BakalavrMalumot.objects.all()
    serializer_class = BakalavrMalumotSerializer



    

class MagistrHujatViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MagistrHujat.objects.all()
    serializer_class = MagistrHujatSerializer

    
class MagistrBolimViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MagistrBolim.objects.all()
    serializer_class = MagistrBolimSerializer

    
class MagistrTolovViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MagistrTolov.objects.all()
    serializer_class = MagistrTolovSerializer

    
class MagistrMalumotViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MagistrMalumot.objects.all()
    serializer_class = MagistrMalumotSerializer

    



class PhdHujatViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PhdHujat.objects.all()
    serializer_class = PhdHujatSerializer

    
class PhdBolimViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PhdBolim.objects.all()
    serializer_class = PhdBolimSerializer

    
class PhdTolovViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PhdTolov.objects.all()
    serializer_class = PhdTolovSerializer

    
class PhdMalumotViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = PhdMalumot.objects.all()
    serializer_class = PhdMalumotSerializer

    



class DscHujatViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = DscHujat.objects.all()
    serializer_class = DscHujatSerializer

    
class DscBolimViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = DscBolim.objects.all()
    serializer_class = DscBolimSerializer

    
class DscTolovViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = DscTolov.objects.all()
    serializer_class = DscTolovSerializer

    
class DscMalumotViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = DscMalumot.objects.all()
    serializer_class = DscMalumotSerializer

    