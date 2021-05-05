from django.db.models import Prefetch
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Guide, GuideVersion
from .permissions import IsAdminOrReadOnly
from .serializers import (ElementSerializer, GuideSerializer,
                          GuideVersionSerializer, VersionDateSerializer)


class GuideViewSet(ReadOnlyModelViewSet):
    serializer_class = GuideSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        queryset = Guide.objects.all()
        input_data = self.request.query_params
        if len(input_data) > 0:  # проверяет, есть ли в параметрах запроса какие-либо данные
            serializer = VersionDateSerializer(data=input_data)
            serializer.is_valid(raise_exception=True)
            search_date = serializer.validated_data.get('search_date', None)
            if search_date is not None:
                guide_vers = GuideVersion.objects.filter(
                    date_from__lte=search_date
                )
                queryset = Guide.objects.prefetch_related(
                    Prefetch('versions', queryset=guide_vers)
                )
        return queryset


class GuideVersionViewSet(ReadOnlyModelViewSet):
    serializer_class = GuideVersionSerializer
    permission_classes = (IsAdminOrReadOnly, )
    filterset_fields = ['name', ]

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
