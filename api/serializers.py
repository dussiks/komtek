from rest_framework import serializers

from .models import Element, Guide, GuideVersion


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('id', 'title', 'description', 'start_date', 'version')
        lookup_field = 'slug'


class GuideVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideVersion
        fields = ('name', 'date_from', 'guide')


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
