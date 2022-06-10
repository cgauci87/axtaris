from django.views.decorators.http import require_http_methods
from scraping.script import aws_scrape, EbayScraper
from stores.utiles import extract_lowest_price, success_response, error_response

@require_http_methods(["GET"])
def search_products(request):
    """ searching product in online store"""
    search_query = request.GET.get('search_query')
    if search_query is None:
        return error_response(message="search_query is required", status_code=400)
    try:
        aws_product_list = list()
        ebay_product_list = list()

        try:
            aws_product_list+=aws_scrape(search_query)
        except Exception as e:
            print("AWS Error:- ", e)
            pass

        try:
            ebay_product_list+=EbayScraper(search_query).scrape_products()
        except:
            pass

        overall_products = aws_product_list + ebay_product_list

        data = {
            "final_lowest_product": extract_lowest_price(overall_products) if len(overall_products) > 0 else dict(),
            "aws_lowest_product": extract_lowest_price(aws_product_list) if len(aws_product_list) > 0 else dict(),
            "ebay_lowest_product": extract_lowest_price(ebay_product_list) if len(ebay_product_list) > 0 else dict(),
            "total_products": overall_products,
        }
        return success_response(data=data, message="Success")
    except Exception as error:
        print("Error:- ", error)
        return error_response()