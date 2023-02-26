from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, PriceData
from .serializers import ProductSerializer, PriceDataSerializer

from web_crawler.scraper import scrape_product_data

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request):
        # print(request.data)
        try:
            url = request.data['url']
            website = request.data['website']
            assert(website in dict(Product.AVAILABLE_CHOICES))
            product_name, product_price = scrape_product_data(url=url, website=website)
            product = Product.objects.create(
                name=product_name, 
                url=url,
                website=website
            )

            price_data = PriceData.objects.create(product=product, price=product_price)
            serializer = ProductSerializer(product)
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED 
            )

        except Exception as e:
            return Response(
                data={
                    'detail': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class PriceDataListView(APIView):
    pagination_class = []
    
    def get(self, request):
        try:
            product_id = request.GET.get('product_id')
            price_datas = PriceData.objects.filter(product_id=product_id).order_by('id')
            serializer = PriceDataSerializer(price_datas, many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                data={
                    'detail': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )