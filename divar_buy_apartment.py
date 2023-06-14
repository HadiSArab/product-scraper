
# scrape data and store all product keys and values
import json,requests

# dictionary to store nested json
dic = {}

# url is a variable to store desired api
# this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
url = 'https://api.divar.ir/v8/posts-v2/web/AZK6h9QY'

resp = requests.get(url)
resp = json.loads(resp.text)
temp = resp['sections'][5]['widgets'][0]['data']['chip_list']['chips'][1]['action']['payload']['web_url']
temp1 = temp.split('/')

dic['city']     = temp1[0]
dic['category'] = temp1[1]
dic['district'] = temp1[2]

if len(resp['sections']) == 10:
    dic['size']     = resp['sections'][9]['widgets'][0]['data']['items'][0]['value']
    dic['year of construction'] = resp['sections'][9]['widgets'][0]['data']['items'][1]['value']
    dic['number of rooms']      = resp['sections'][9]['widgets'][0]['data']['items'][2]['value'] 
    dic['floor']      = resp['sections'][9]['widgets'][5]['data']['value'].split(" ")[0]

    if resp['sections'][9]['widgets'][7]['data']['items'][0]['available']:
        dic['elevator'] = 'yes'
    else:
        dic['elevator'] = 'no'


    if resp['sections'][9]['widgets'][7]['data']['items'][1]['available']:
        dic['parking'] = 'yes'
    else:
        dic['parking'] = 'no'


    if resp['sections'][9]['widgets'][7]['data']['items'][2]['available']:
        dic['storage'] = 'yes'
    else:
        dic['storage'] = 'no'

    dic['price per meter']      = resp['sections'][9]['widgets'][2]['data']['value']
    dic['total price']      = resp['sections'][9]['widgets'][1]['data']['value']

else:
    dic['size']     = resp['sections'][8]['widgets'][0]['data']['items'][0]['value']
    dic['year of construction'] = resp['sections'][8]['widgets'][0]['data']['items'][1]['value']
    dic['number of rooms']      = resp['sections'][8]['widgets'][0]['data']['items'][2]['value'] 
    dic['floor']      = resp['sections'][8]['widgets'][5]['data']['value'].split(" ")[0]

    if resp['sections'][8]['widgets'][7]['data']['items'][0]['available']:
        dic['elevator'] = 'yes'
    else:
        dic['elevator'] = 'no'


    if resp['sections'][8]['widgets'][7]['data']['items'][1]['available']:
        dic['parking'] = 'yes'
    else:
        dic['parking'] = 'no'


    if resp['sections'][8]['widgets'][7]['data']['items'][2]['available']:
        dic['storage'] = 'yes'
    else:
        dic['storage'] = 'no'
        
    dic['price per meter']      = resp['sections'][8]['widgets'][2]['data']['value']
    dic['total price']      = resp['sections'][8]['widgets'][1]['data']['value']






with open ('divar.json','w') as l:
    json.dump(dic,l)

# dic:{city:"",
#      category:"",
#      district:"",
#      size:"",
#      year of construction:"",
#      number of rooms:"",
#      total price :"",
#      price per meter:"",
#      floor:"",
#      facilities:{elevator:"",
#                  storage:"",
#                  parking:"",
    
#      }

# }