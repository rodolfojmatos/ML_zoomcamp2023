import requests


url = 'http://127.0.0.1:9696/predict'


customer = {"job": "unknown", "duration": 270, "poutcome": "failure"}


response = requests.post(url, json=customer).json()

print(response)