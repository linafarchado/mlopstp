import requests

url = "http://localhost:8000/predict"
data = {
    "size": 5000,
    "bedrooms": 3,
    "has_garden": True
}

response = requests.post(url, json=data)
print(response.json())