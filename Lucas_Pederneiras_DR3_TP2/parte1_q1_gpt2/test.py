import requests

url = "http://localhost:8000/generate"
data = {"text": "Once upon a time"}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
