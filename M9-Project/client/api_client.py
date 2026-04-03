import requests

# This is the address where your FastAPI backend is running
BASE_URL = "http://127.0.0.1:8000"

def get_inventory():
    response = requests.get(f"{BASE_URL}/inventory/")
    if response.status_code == 200:
        return response.json()
    return []

def add_item(name, quantity, expiry_date):
    data = {
        "name": name, 
        "quantity": quantity, 
        "expiry_date": str(expiry_date)
    }
    response = requests.post(f"{BASE_URL}/inventory/", json=data)
    if response.status_code == 200:
        return response.json()
    return None

def get_recipes():
    response = requests.get(f"{BASE_URL}/recipes/suggest")
    if response.status_code == 200:
        return response.json()
    return {"error": "Could not connect to backend"}