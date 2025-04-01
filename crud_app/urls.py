from rest_framework.routers import DefaultRouter
from .views import TareaViewSet
router = DefaultRouter()
router.register(r'Tareas', TareaViewSet, basename = 'tarea')
urlpatterns = router.urls
