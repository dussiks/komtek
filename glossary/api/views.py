from rest_framework import viewsets, filters

from .models import Guide, Element
from .serializers import GuideSerializer


class GuideViewSet(viewsets.ModelViewSet):
    serializer_class = GuideSerializer
    queryset = Guide.objects.all()
    search_fields = ['version', ]
