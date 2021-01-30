from rest_framework.routers import SimpleRouter

from .views import ClientViewSet

router_client = SimpleRouter()
router_client.register('clients', ClientViewSet)
