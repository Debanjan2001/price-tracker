from bs4 import BeautifulSoup
import requests
import json

HEADERS = {
    'User-Agent': ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"),
    'Accept-Language': 'en-US, en;q=0.5'
}

def scrape_amazon_product(url):
    """
    Returns title, price
    """
    resp = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, features='lxml')
    title = soup.find('span', {'id':"productTitle"}).text.strip()
    price = soup.find('span', {'class':"a-price-whole"}).text.strip()
    price = "".join(ch for ch in price if ch.isdigit())
    return title, price 

def scrape_myntra_product(url):
    resp = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, features='lxml')
    
    script = None
    for s in soup.find_all("script"):
        if 'pdpData' in s.text:
            script = s.get_text(strip=True)
            break
            
    data=json.loads(script[script.index('{'):])
    title = data['pdpData']['name']
    price = data['pdpData']['sizes'][0]['sizeSellerData'][0]['discountedPrice']
    return title, price

SCRAPING_FUNCTION_MAPPER = {
    'AMAZON': scrape_amazon_product,
    'MYNTRA': scrape_myntra_product,
}

def scrape_price(url, website):
    my_scraper_func = SCRAPING_FUNCTION_MAPPER[website]
    return my_scraper_func(url)
