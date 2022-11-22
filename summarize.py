import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer "}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

input = str(input())

output = query({
    "inputs": input
})

print(output)