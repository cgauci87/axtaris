from selectorlib import Extractor
import requests
from pathlib import Path
import json
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file(f'{BASE_DIR}/scraping/search_results.yml')

def aws_scrape(product_name):
    aws_product = list()
    url = f"https://www.amazon.com/s?k={product_name}"
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    # Download the page using requests
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create
    for product in e.extract(r.text)['products']:
        if product['price'] == None or product['price'] == "None":
            continue
        aws_product.append(
            {
                "title": product['title'],
                "price": float(product['price'].replace("$", "").replace(",", "")),
                "url": f"https://www.amazon.com{product['url']}",
            }
        )
    return aws_product


class EbayScraper:

    def __init__(self, keyword):
        self.keyword = keyword
        plusified_keyword = keyword.replace(" ", "+")
        self.products = []
        self.search_url = "https://www.ebay.com/sch/i.html?_nkw=" + plusified_keyword

    def scrape_products(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        content = requests.get(self.search_url, headers=headers).text
        soup = BeautifulSoup(content, "html.parser")
        product_list = []
        products = soup.find("ul", {"class": "srp-results srp-list clearfix"}).find_all("li", {"class": "s-item s-item__pl-on-bottom"})
        for product in products:
            div = product.find("div", {"class": "s-item__info clearfix"})
            name = div.find('h3', {'class': 's-item__title'}).text
            price = div.find('span', {"class": "s-item__price"}).text
            url = div.find('a', {"class": "s-item__link"})['href']

            try:
                product_price = float(price.replace("$", "").replace(",", ""))
            except:
                product_price = float(price.split(" ")[0].replace("$", "").replace(",", ""))

            product_list.append({
                "title": name,
                "price": product_price,
                "url": url
            })
        return product_list

    def ebay_product_search_api_call(self):
        ebey_product = []
        EBEY_API_KEY = "65fecbec9f36d301706583f1ee3bdb4b8bb9e99901989d6453e27d1ec9640211"
        EBEY_API_URL = f"https://serpapi.com/search.json?engine=ebay&_nkw={self.plusified_keyword}&api_key={EBEY_API_KEY}"
        response = requests.get(EBEY_API_URL)
        data = json.loads(response.text)
        for product_data in data.get("organic_results")[:10]:
            ebey_product.append(
                {
                    "title": product_data.get("title"),
                    "price": product_data.get("price").get("raw"),
                    "url": product_data.get("url"),
                }
            )
        return ebay_product

