from rest_framework.serializers import ModelSerializer
from collection.models import Item, ItemSpec, ItemKind
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'patrimony',
        )

class ItemSpecSerializer(ModelSerializer):
    items_available = serializers.SerializerMethodField()
    items_total = serializers.SerializerMethodField()

    def get_items_available(self, obj):
        items = Item.objects.filter(
                spec=obj).filter(
                        loan_items__isnull=True)
        return ItemSerializer(items, many=True).data

    def get_items_total(self, obj):
        return Item.objects.filter(
                spec=obj).count()

    class Meta:
        model = ItemSpec
        fields = (
            'id',
            'name',
            'description',
            'items_available',
            'items_total',
        )


class ItemKindSerializer(ModelSerializer):
    spec_kind = ItemSpecSerializer(many=True, read_only=True)

    class Meta:
        model = ItemKind
        fields = (
            'id',
            'name',
            'description',
            'spec_kind',
        )

class ItemGetSerializer(ModelSerializer):
    spec = serializers.StringRelatedField(read_only=True)
    kind = serializers.SerializerMethodField()

    def get_kind(self,obj):
        return obj.spec.kind.name

    class Meta:
        model = Item
        fields = (
            'id',
            'patrimony',
            'spec',
            'kind',
        )
