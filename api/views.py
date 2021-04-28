from django_filters.rest_framework import FilterSet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Element, Guide, GuideVersion
from .permissions import IsAdminOrReadOnly
from .serializers import ElementSerializer, GuideSerializer


class GuideViewSet(viewsets.ModelViewSet):
    serializer_class = GuideSerializer
    queryset = Guide.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    search_fields = ['start_date', ]
    lookup_field = 'slug'


class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        guide = get_object_or_404(Guide, pk=self.kwargs.get('guide_id'))
        version = get_object_or_404(GuideVersion, pk=self.kwargs.get('guideversion_id'))
        queryset = version.elements.all()
        return queryset
