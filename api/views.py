from django_filters.rest_framework import FilterSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Element, Guide, GuideVersion
from .permissions import IsAdminOrReadOnly
from .serializers import (
    ElementSerializer, GuideSerializer, GuideVersionSerializer
)


class GuideViewSet(ReadOnlyModelViewSet):
    serializer_class = GuideSerializer
    queryset = Guide.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    search_fields = ['start_date', ]


class GuideVersionViewSet(ReadOnlyModelViewSet):
    serializer_class = GuideVersionSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        guide = get_object_or_404(Guide, pk=self.kwargs.get('guide_id'))
        queryset = guide.versions.all()
        return queryset


class ElementViewSet(ReadOnlyModelViewSet):
    serializer_class = ElementSerializer
    permission_classes = (IsAdminOrReadOnly, )

    @action(detail=False)
    def get_queryset(self):
        guide = get_object_or_404(Guide, pk=self.kwargs.get('guide_id'))
        version = GuideVersion.objects.get(guide_unique=guide.id)
        queryset = version.elements.all()
        return queryset
