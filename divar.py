
# scrape data and store all product keys and values
import json,requests

# url is a variable to store desired api
# this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
url = 'https://api.divar.ir/v8/posts-v2/web/AZJGY6xy'

resp = requests.get(url)
resp = json.loads(resp.text)
print(resp)
