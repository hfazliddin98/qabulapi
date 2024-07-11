
from rest_framework.routers import SimpleRouter
from .views import ArizaViewSet, QolanmaViewSet



router = SimpleRouter()

router.register('ariza', ArizaViewSet, basename='ariza')
router.register('qolanma', QolanmaViewSet, basename='qolanma')


urlpatterns = []
urlpatterns += router.urls
