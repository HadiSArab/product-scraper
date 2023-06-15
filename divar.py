
# scrape data and store all product keys and values
import json,requests

# this is last dictionary to store
dic ={}
tags_loc =0
list_data_loc = 0

# url is a variable to store desired api
# this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
url = 'https://api.divar.ir/v8/posts-v2/web/AZr9g52S'

resp = requests.get(url)
resp = json.loads(resp.text)

for i in range(len(resp['sections'])):
    if resp['sections'][i]['section_name'] == "TAGS":
         tags_loc = i

    if resp['sections'][i]['section_name'] == "LIST_DATA":
         list_data_loc = i


if 'available' in resp['sections'][list_data_loc]['widgets'][7]['data']['items'][1].keys():
    print('yes')
else:
    print('no')

print("list_data ",list_data_loc)
print("tags ",tags_loc)