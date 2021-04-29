from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import get_object_or_404

from .models import Guide, GuideVersion
from .permissions import IsAdminOrReadOnly
from .serializers import (
    ElementSerializer, GuideSerializer, GuideVersionSerializer
)


class GuideViewSet(ReadOnlyModelViewSet):
    serializer_class = GuideSerializer
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Guide.objects.all()


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

    def get_queryset(self):
        guide_version = get_object_or_404(
            GuideVersion,
            pk=self.kwargs.get('version_id')
        )
        queryset = guide_version.elements.all()
        return queryset
