import requests, json

url = 'https://api.divar.ir/v8/web-search/tehran/buy-apartment'
resp = requests.get(url)
resp = json.loads(resp.text)

x = []
for i in range(23):
    x.append(resp['web_widgets']['post_list'][i]['data']['token'])

print(x)