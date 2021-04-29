from rest_framework import serializers

from .models import Element, Guide, GuideVersion


class GuideSerializer(serializers.ModelSerializer):
    start_date = serializers.ReadOnlyField()
    version = serializers.ReadOnlyField()

    class Meta:
        model = Guide
        fields = ('id', 'title', 'description', 'start_date', 'version')


class GuideVersionSerializer(serializers.ModelSerializer):
    guide = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='slug',
    )

    class Meta:
        model = GuideVersion
        fields = ('name', 'date_from', 'guide', 'guide_unique')


class ElementSerializer(serializers.ModelSerializer):
    version = GuideVersionSerializer(many=True, read_only=True)

    class Meta:
        model = Element
        fields = ('code', 'value', 'version')
