import requests


url = 'http://127.0.0.1:9696/predict'


customer = {"job": "retired", "duration": 445, "poutcome": "success"}


response = requests.post(url, json=customer).json()

print(response)