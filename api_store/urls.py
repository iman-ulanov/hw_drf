from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from store import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/category/', views.create_category),
    path('store/brand/', views.create_brand),
    path('store/product/', views.create_product),

    path('store/category/<int:pk>', views.detail_category),
    path('store/brand/<int:pk>', views.detail_brand),
    path('store/product/<int:pk>', views.detail_product),
]
