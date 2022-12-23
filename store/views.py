import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics

from .models import Products, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_category = Category.objects.create(**data)
        json_data = {
            "name": new_category.name
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        categories = Category.objects.all()
        data = []
        for cat in categories:
            data.append(
                {
                    'name': cat.name,
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


class DeleteCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandCreateListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
