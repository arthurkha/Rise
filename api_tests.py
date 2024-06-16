import requests

base_url = "https://fakestoreapi.com"

def test_get_all_products():
  """Retrieving all products"""
  url = f"{base_url}/products"
  response = requests.get(url)
  assert response.status_code == 200
  assert isinstance(response.json(), list)

def test_get_product_by_id():
  """Retrieving product by ID"""
  product_id = 1
  url = f"{base_url}/products/{product_id}"
  response = requests.get(url)
  assert response.status_code == 200
  assert "id" in response.json()
  assert response.json()["id"] == product_id

def test_create_product():
  """Create new product"""
  url = f"{base_url}/products"
  data = {
    "title": "Test Product",
    "price": 100,
    "description": "Test product",
    "category": "electronics",
    "image": "https://google.com/new-product.jpg"
  }
  response = requests.post(url, json=data)
  assert response.status_code == 200

def test_delete_product():
  """Delete product"""
  product_id = 1
  url = f"{base_url}/products/{product_id}"
  response = requests.delete(url)
  assert response.status_code == 200

def test_get_nonexistent_product():
  """Retrieve non-existent product"""
  nonexistent_id = 222
  url = f"{base_url}/products/{nonexistent_id}"
  response = requests.get(url)
  assert response.status_code == 200

def test_invalid_get_request():
  """Invalid endpoint"""
  invalid_url = f"{base_url}/invalid_endpoint"
  response = requests.get(invalid_url)
  assert response.status_code >= 400

def test_post_no_data():
  """POST request with no data"""
  url = f"{base_url}/products"
  data = {}
  response = requests.post(url, json=data)
  assert response.status_code >= 200

def test_delete_nonexistent_product():
  """Delete non-existent product"""
  nonexistent_id = 222
  url = f"{base_url}/products/{nonexistent_id}"
  response = requests.delete(url)
  assert response.status_code == 200

if __name__ == "__main__":
  test_get_all_products()
  test_get_product_by_id()
  test_create_product()
  test_delete_product()
  test_get_nonexistent_product()
  test_invalid_get_request()
  test_post_no_data()
  test_delete_nonexistent_product()
print("All tests passed!")
