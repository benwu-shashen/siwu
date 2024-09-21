import requests

r = requests.get('http://jsonplaceholder.typicode.com/posts')
print(r.status_code)
print(r.json())