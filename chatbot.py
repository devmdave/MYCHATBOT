
import requests

# Define the API endpoint and your API key
url = "http://localhost:11434/api/generate"

payload = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Why is the sky blue?",
    "stream": False

}

# Make the POST request
response = requests.post(url, json=payload)
print(response.json()["response"])
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     print("Response from Ollama:", data)
# else:
#     print("Failed to get a response. Status code:", response.status_code)
#     print("Response:", response.text)
