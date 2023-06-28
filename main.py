from woocommerce import API
import os

# API AUTHENTICATION
wcapi = API(
    url="https://shop.biruke.com",
    consumer_key= os.environ.get('C_KEY'),
    consumer_secret=os.environ.get("C_SECRET"),
    wp_api=True,
    version="wc/v3"
)

# GET A LIST OF ALL PRODUCTS
# Based on WC API documentation, there is a max limit which is 100 products per call (per_page)
# I CREATED PRODUCTS WITHOUT PRICES & MY TOTAL NUMBER OF PRODUCTS ARE NOW 108(78 WITH PRICE AND 30 WITHOUT)

# LOOP THROUGH PAGES AND GET ALL PRODUCTS
page = 1
all_products = []
while  True:
    products = wcapi.get('products', params={'per_page': 100 , 'page': page}).json()

    for prods in products:
        all_products.append(prods)
    if len(products) == 0:
        break

    page +=1

# FILTER OUT ALL PRODUCTS WITHOUT PRICE

prods_without_price = [ product for product in all_products if product['price']=='']

#GET THE ID OF PRODUCTS WITHOUT PRICE

prods_without_price_id = [x['id'] for x in prods_without_price ]

# MAKE A DELETE API CALL BASED ON THE ID LISTED ABOVE

for id in prods_without_price_id:
    wcapi.delete(f"products/{id}", params={"force": True}).json()

# the end












