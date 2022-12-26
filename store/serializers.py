from rest_framework import serializers

from .models import Brand, Category, Products


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    price = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        product = Products.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            brand_id=validated_data['brand_id'],
            category_id=validated_data['category_id']
        )
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.brand_id = validated_data['brand_id']
        instance.category_id = validated_data['category_id']
        instance.save()
        return instance


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    address = serializers.CharField(max_length=40)


    def create(self, validated_data):
        brand = Brand.objects.create(
            name=validated_data['name'],
            address=validated_data['address']
        )
        return brand

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance



class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)


    def create(self, validated_data):
        category = Category.objects.create(
            name=validated_data['name'],
        )
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance

