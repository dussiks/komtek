from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GuideViewSet, ElementViewSet


v1_router = DefaultRouter()
v1_router.register('guides', GuideViewSet, basename='guides')
v1_router.register(
    r'guides/(?P<slug>\d+)/elements',
    ElementViewSet,
    basename='elements',
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
