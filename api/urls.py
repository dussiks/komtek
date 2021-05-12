from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ElementViewSet, GuideViewSet, GuideVersionViewSet, actual_elements


v1_router = DefaultRouter()
v1_router.register('guides', GuideViewSet, basename='guides')
v1_router.register(
    r'guides/(?P<guide_id>\d+)/versions',
    GuideVersionViewSet,
    basename='versions',
)
v1_router.register(
    r'guides/(?P<guide_id>\d+)/versions/(?P<version_id>\d+)/elements',
    ElementViewSet,
    basename='elements',
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/guides/<int:guide_id>/elements/', actual_elements, name='actual')
]
