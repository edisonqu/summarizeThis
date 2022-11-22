import requests
import dotenv
import os
dotenv.load_dotenv()

API_KEY_HF = os.getenv("API_KEY_HF")


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_KEY_HF}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# output = query({
#     "inputs": input
# })
#
# print(output)