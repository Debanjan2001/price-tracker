from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PriceDataListView

app_name = 'product'

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('price_datas/', PriceDataListView.as_view(), name='price-datas')
]