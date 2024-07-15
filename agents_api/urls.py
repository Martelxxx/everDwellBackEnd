from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'agents', views.AgentViewSet)
router.register(r'homes', views.HomeViewSet)
router.register(r'buyers', views.BuyerViewSet)

urlpatterns = [
    path('agent/', views.agent_view, name='agent_view'),
    path('', include(router.urls)),  # This includes router URLs in the urlpatterns
    path('home/', views.home_view, name='home_view'),
    path('buyer/', views.buyer_view, name='buyer_view'),
]