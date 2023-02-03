from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web_crawler.serializers import PriceQuerySerializer
from web_crawler.utils import scrape_price

# Create your views here.
@api_view(['GET'])
def query_price(request):

    serializer = PriceQuerySerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            data={
                'detail':'Bad Request'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # print(serializer.data['url'])

    try:
        title, price = scrape_price(
            url=serializer.data['url'], 
            website=serializer.data['website']
        )
    except:
        return Response(
            data={
                'detail':'Some Error Occurred! Please try again later...'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    return Response(
        data={
            'message':'Success',
            'title':title,
            'price':price,
        },
        status=status.HTTP_200_OK,
    )