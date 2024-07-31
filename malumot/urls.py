from rest_framework.routers import SimpleRouter
from .views import BakalavrHujatViewSet, BakalavrBolimViewSet, BakalavrTolovViewSet, BakalavrMalumotViewSet
from .views import MagistrHujatViewSet, MagistrBolimViewSet, MagistrTolovViewSet, MagistrMalumotViewSet
from .views import PhdHujatViewSet, PhdBolimViewSet, PhdTolovViewSet, PhdMalumotViewSet
from .views import DscHujatViewSet, DscBolimViewSet, DscTolovViewSet, DscMalumotViewSet



router = SimpleRouter()

router.register('bakalavr_royhat', BakalavrHujatViewSet, basename='bakalavr_royhat')
router.register('bakalavr_mudat', BakalavrBolimViewSet, basename='bakalavr_mudat')
router.register('bakalavr_tolov', BakalavrTolovViewSet, basename='bakalavr_tolov')
router.register('bakalavr_toliq_malumot', BakalavrMalumotViewSet, basename='bakalavr_toliq_malumot')


router.register('magistr_royhat', MagistrHujatViewSet, basename='magistr_royhat')
router.register('magistr_mudat', MagistrBolimViewSet, basename='magistr_mudat')
router.register('magistr_tolov', MagistrTolovViewSet, basename='magistr_tolov')
router.register('magistr_toliq_malumot', MagistrMalumotViewSet, basename='magistr_toliq_malumot')


router.register('phd_royhat', PhdHujatViewSet, basename='phd_royhat')
router.register('phd_mudat', PhdBolimViewSet, basename='phd_mudat')
router.register('phd_tolov', PhdTolovViewSet, basename='phd_tolov')
router.register('phd_toliq_malumot', PhdMalumotViewSet, basename='phd_toliq_malumot')


router.register('dsc_royhat', DscHujatViewSet, basename='dsc_royhat')
router.register('dsc_mudat', DscBolimViewSet, basename='dsc_mudat')
router.register('dsc_tolov', DscTolovViewSet, basename='dsc_tolov')
router.register('dsc_toliq_malumot', DscMalumotViewSet, basename='dsc_toliq_malumot')


urlpatterns = []
urlpatterns += router.urls