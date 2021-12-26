import requests 
import json
api_url = "https://jsonplaceholder.typicode.com/todos/1"

#responde = requests.get(api_url)


todo = {"userId":1,"title":"Buy milk","completed":False}

response = requests.post(api_url, json=todo)

print(response.json())
print(response.status_code)

#print(response.headers["content-Type"])