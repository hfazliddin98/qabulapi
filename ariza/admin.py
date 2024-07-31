from django.contrib import admin
from .models import Ariza, Qolanma
from .models import BakalavrHujat, BakalavrBolim, BakalavrTolov, BakalavrMalumot
from .models import MagistrHujat, MagistrBolim, MagistrTolov, MagistrMalumot
from .models import PhdHujat, PhdBolim, PhdTolov, PhdMalumot
from .models import DscHujat, DscBolim, DscTolov, DscMalumot



admin.site.register([Ariza, Qolanma])
admin.site.register([BakalavrHujat, BakalavrBolim, BakalavrTolov, BakalavrMalumot])
admin.site.register([MagistrHujat, MagistrBolim, MagistrTolov, MagistrMalumot])
admin.site.register([PhdHujat, PhdBolim, PhdTolov, PhdMalumot])
admin.site.register([DscHujat, DscBolim, DscTolov, DscMalumot])