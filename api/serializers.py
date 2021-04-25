from rest_framework import serializers

from .models import Guide, Element


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
