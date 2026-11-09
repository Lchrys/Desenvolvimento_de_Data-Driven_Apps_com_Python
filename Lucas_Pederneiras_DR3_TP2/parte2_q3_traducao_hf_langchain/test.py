import requests

url = "http://localhost:8000/translate"
data = {"text": "Hello, how are you?"}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
