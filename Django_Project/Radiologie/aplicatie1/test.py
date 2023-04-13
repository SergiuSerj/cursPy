import requests

url = f'https://api.exchangerate.host/convert?from=RON&to=EUR&amount=100'
response = requests.get(url)
data = response.json()
# print(data)
result = data['result']
print(result)
