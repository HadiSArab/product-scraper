
# scrape data and store all product keys and values
import json,requests

# dictionary to store nested json
dic = {}

# url is a variable to store desired api
# this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
url = 'https://api.divar.ir/v8/posts-v2/web/AZK6h9QY'

resp = requests.get(url)
resp = json.loads(resp.text)
floor = resp['sections'][9]['widgets'][5]['data']['value']
x = floor.split(" ")[0]
print(x)

