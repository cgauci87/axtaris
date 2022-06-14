from selectorlib import Extractor
import requests
from pathlib import Path
import json
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file(f'{BASE_DIR}/scraping/search_results.yml')

# Flipkart Scaper - To obtain data from the source itself
class FlipkartScraper:

    def __init__(self, keyword):
        self.keyword = keyword
        plusified_keyword = keyword.replace(" ", "+")
        self.products = []
        self.search_url = "https://www.flipkart.com/search?q=" + plusified_keyword

    def scrape_products(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        content = requests.get(self.search_url, headers=headers).text
        soup = BeautifulSoup(content, "html.parser")
        product_list = []
        products = soup.find("div", {"class": "_1YokD2 _3Mn1Gg"}).find_all("div", {"class": "_1AtVbE col-12-12"})
        for product in products:
            try:
                div = product.find("div", {"class": "_13oc-S"})
                url = f'https://www.flipkart.com{div.div.div.a["href"]}'
                name = div.find('div', {'class': '_4rR01T'}).text
                price = div.find('div', {"class": "_30jeq3 _1_WHN1"}).text

                product_list.append({
                    "title": name,
                    "price": round(float(price.replace("₹", "").replace(",", ""))/77.55, 2),
                    "url": url
                })
            except:
                pass
        return product_list

# Ebay Scaper - To obtain data from the source itself
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

