import requests

# print(requests.get("http://127.0.0.1:8000/parts/?manufacturer=Ammann").json())
print(requests.get("http://127.0.0.1:8000/parts/?manufacturer=Ammann&category=Excavator%20parts/56").json())

