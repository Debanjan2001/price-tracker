from web_crawler.scraper import scrape_product_data
from .models import PriceData, Product

def get_price(*args, **kwargs):
    try:
        website = kwargs['website']
        url = kwargs['url']
        product_id = kwargs['product_id']
        _, product_price = scrape_product_data(url=url, website=website)
        PriceData.objects.create(product_id=product_id, price=product_price)
    except:
        # Ideally I should start logging the error message here,
        # But lets assume no error occurs
        return