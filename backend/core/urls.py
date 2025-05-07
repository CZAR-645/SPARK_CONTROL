from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, EquipamentoViewSet, AluguelViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'alugueis', AluguelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]