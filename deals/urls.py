from rest_framework.routers import DefaultRouter
from .views import DealViewSet

router = DefaultRouter()
router.register(r'deals',DealViewSet)

urlpatterns = router.urls