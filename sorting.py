# Step 1: import requests library
import requests

# Step 2: API URL
url = "https://fakestoreapi.com/products?limit=5"

# Step 3: send request to API
response = requests.get(url)

# Step 4: convert response to JSON (list of products)
products = response.json()

# Step 5: sort products based on rating (highest first)
sorted_products = sorted(products, key=lambda x: x["rating"]["rate"], reverse=True)

# Step 6: print sorted products
for product in sorted_products:
    print("Title:", product["title"])
    print("Rating:", product["rating"]["rate"])
    print("-" * 30)