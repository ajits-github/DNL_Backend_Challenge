import requests

# BASE_URL = "http://127.0.0.1:8000"

# def test_get_parts():
#     manufacturer_name = "Ammann"
#     response = requests.get(f"{BASE_URL}/parts/?manufacturer={manufacturer_name}")
    
#     assert response.status_code == 200
#     # Further checks can be added based on expected response content


from fastapi.testclient import TestClient
from api.api_server import app

client = TestClient(app)

def test_get_parts():
    response = client.get("/parts/?manufacturer=Ammann")
    assert response.status_code == 200