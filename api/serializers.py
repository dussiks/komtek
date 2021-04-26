from rest_framework import serializers

from .models import Guide, Element


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('title', 'description', 'start_date', 'version')


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
