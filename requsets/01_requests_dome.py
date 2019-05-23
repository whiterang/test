import requests

url = "http://118.24.29.59:5000/"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "88cf5145-d9fc-4a98-9e1f-b07d36bff5b2"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)