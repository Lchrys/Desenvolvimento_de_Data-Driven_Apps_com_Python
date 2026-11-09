import requests

url = "http://localhost:8000/chat"
data = {"message": "Em qual continente fica o Brasil?"}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
