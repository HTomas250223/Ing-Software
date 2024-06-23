from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AulaViewSet, DocenteViewSet, HorarioViewSet

router = DefaultRouter()
router.register(r'aulas', AulaViewSet)
router.register(r'docentes', DocenteViewSet)
router.register(r'horarios', HorarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
