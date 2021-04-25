from rest_framework import viewsets, filters
from rest_framework.generics import get_object_or_404

from .models import Guide, Element
from .serializers import GuideSerializer, ElementSerializer


class GuideViewSet(viewsets.ModelViewSet):
    serializer_class = GuideSerializer
    queryset = Guide.objects.all()
    search_fields = ['version', ]


class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer

    def get_queryset(self):
        guide = get_object_or_404(Guide, pk=self.kwargs.get('guide_id'))
        queryset = Guide.elements.all()
        return queryset
