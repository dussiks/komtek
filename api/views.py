from django_filters.rest_framework import FilterSet
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from .models import Element, Guide, GuideVersion
from .permissions import IsAdminOrReadOnly
from .serializers import ElementSerializer, GuideSerializer


class GuideVersionFilter(FilterSet):
    class Meta:
        model = GuideVersion
        fields = {
            'date_from': ['exact', 'day__gt'],
        }


class GuideViewSet(viewsets.ModelViewSet):
    serializer_class = GuideSerializer
    queryset = Guide.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    search_fields = ['version', ]
    lookup_field = 'slug'


class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer

    def get_queryset(self):
        guide = get_object_or_404(Guide, pk=self.kwargs.get('guide_id'))
        queryset = Guide.elements.all()
        return queryset
