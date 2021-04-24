from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GuideViewSet


v1_router = DefaultRouter()
v1_router.register('guides', GuideViewSet, basename='guides')
urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
