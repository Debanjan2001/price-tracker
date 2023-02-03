from django.urls import path
from web_crawler import views

app_name = 'web_crawler'

urlpatterns = [
    path('', views.query_price, name='price-query'),
]