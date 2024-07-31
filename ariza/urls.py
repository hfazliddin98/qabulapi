
from rest_framework.routers import SimpleRouter
from .views import ArizaViewSet, QolanmaViewSet
from .views import BakalavrHujatViewSet, BakalavrBolimViewSet, BakalavrTolovViewSet, BakalavrMalumotViewSet
from .views import MagistrHujatViewSet, MagistrBolimViewSet, MagistrTolovViewSet, MagistrMalumotViewSet
from .views import PhdHujatViewSet, PhdBolimViewSet, PhdTolovViewSet, PhdMalumotViewSet
from .views import DscHujatViewSet, DscBolimViewSet, DscTolovViewSet, DscMalumotViewSet



router = SimpleRouter()

router.register('ariza', ArizaViewSet, basename='ariza')
router.register('qolanma', QolanmaViewSet, basename='qolanma')


router.register('bakalavr_hujat', BakalavrHujatViewSet, basename='bakalavr_hujat')
router.register('bakalavr_bolim', BakalavrBolimViewSet, basename='bakalavr_bolim')
router.register('bakalavr_tolov', BakalavrTolovViewSet, basename='bakalavr_tolov')
router.register('bakalavr_malumot', BakalavrMalumotViewSet, basename='bakalavr_malumot')


router.register('magistr_hujat', MagistrHujatViewSet, basename='magistr_hujat')
router.register('magistr_bolim', MagistrBolimViewSet, basename='magistr_bolim')
router.register('magistr_tolov', MagistrTolovViewSet, basename='magistr_tolov')
router.register('magistr_malumot', MagistrMalumotViewSet, basename='magistr_malumot')


router.register('phd_hujat', PhdHujatViewSet, basename='phd_hujat')
router.register('phd_bolim', PhdBolimViewSet, basename='phd_bolim')
router.register('phd_tolov', PhdTolovViewSet, basename='phd_tolov')
router.register('phd_malumot', PhdMalumotViewSet, basename='phd_malumot')


router.register('dsc_hujat', DscHujatViewSet, basename='dsc_hujat')
router.register('dsc_bolim', DscBolimViewSet, basename='dsc_bolim')
router.register('dsc_tolov', DscTolovViewSet, basename='dsc_tolov')
router.register('dsc_malumot', DscMalumotViewSet, basename='dsc_malumot')




urlpatterns = []
urlpatterns += router.urls
