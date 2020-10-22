from rest_framework import routers

from .views import NoteViewSet


# Создание router и регистрация ViewSet
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls
