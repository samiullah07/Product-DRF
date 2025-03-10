import requests


request = requests.get("http://127.0.0.1:8000/api/")

# request = requests.get("http://127.0.0.1:8000/api/generics/1")

print(request.json())