from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ElementViewSet, GuideViewSet, GuideVersionViewSet


v1_router = DefaultRouter()
v1_router.register('guides', GuideViewSet, basename='guides')
v1_router.register(
    r'guides/(?P<guide_id>\d+)/versions',
    GuideVersionViewSet,
    basename='version',
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
