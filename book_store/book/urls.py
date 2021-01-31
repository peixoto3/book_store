from rest_framework.routers import SimpleRouter

from .views import BookViewSet

router_book = SimpleRouter()
router_book.register('books', BookViewSet)
