from rest_framework import serializers

from .models import Brand, Category, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=40)
#     price = serializers.IntegerField()
#     brand = serializers.IntegerField()
#     category = serializers.IntegerField()
#
#
# class BrandSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=40)
#     address = serializers.CharField(max_length=40)
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=40)