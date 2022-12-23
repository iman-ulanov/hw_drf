from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from store import views

router = routers.DefaultRouter()
router.register('prods', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/v-1.0/', include(router.urls)),
    path('store/category/', views.create_category),
    path('category/<int:pk>/delete', views.DeleteCategory.as_view()),
    path('category/<int:pk>/delete', views.DeleteCategory.as_view()),
    path('store/brand/', views.BrandCreateListView.as_view()),
    path('store/brand/<int:pk>/', views.BrandRetrieveUpdateDestroyApiView.as_view())
]
