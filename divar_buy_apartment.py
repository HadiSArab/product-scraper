
# scrape data and store all product keys and values
import json,requests
import time 

# this is last dictionary to store
main_dic ={}

def product(i):
        
    # dictionary to store nested json
    dic = {}
    list_data_loc = 0
    tags_loc = 0

    # url is a variable to store desired api
    # this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
    url = 'https://api.divar.ir/v8/posts-v2/web/{}'.format(i)

    resp = requests.get(url)
    resp = json.loads(resp.text)

    for i in range(len(resp['sections'])):
        if resp['sections'][i]['section_name'] == "TAGS":
            tags_loc = i

        if resp['sections'][i]['section_name'] == "LIST_DATA":
            list_data_loc = i

    widgets_len = len(resp['sections'][list_data_loc]['widgets'])

    temp = resp['sections'][tags_loc]['widgets'][0]['data']['chip_list']['chips'][1]['action']['payload']['web_url']
    temp1 = temp.split('/')

    dic['city']     = temp1[0]
    dic['category'] = temp1[1]
    dic['district'] = temp1[2]


    dic['size']     = resp['sections'][list_data_loc]['widgets'][0]['data']['items'][0]['value']
    dic['year of construction'] = resp['sections'][list_data_loc]['widgets'][0]['data']['items'][1]['value']
    dic['number of rooms']      = resp['sections'][list_data_loc]['widgets'][0]['data']['items'][2]['value'] 
    dic['floor']      = resp['sections'][list_data_loc]['widgets'][widgets_len-3]['data']['value'].split(" ")[0]

    if 'available' in resp['sections'][list_data_loc]['widgets'][widgets_len-1]['data']['items'][0].keys():
        dic['elevator'] = 'yes'
    else:
        dic['elevator'] = 'no'


    if 'available' in resp['sections'][list_data_loc]['widgets'][widgets_len-1]['data']['items'][1].keys():
        dic['parking'] = 'yes'
    else:
        dic['parking'] = 'no'


    if 'available' in resp['sections'][list_data_loc]['widgets'][widgets_len-1]['data']['items'][2].keys():
        dic['storage'] = 'yes'
    else:
        dic['storage'] = 'no'

    dic['price per meter']      = resp['sections'][list_data_loc]['widgets'][2]['data']['value']
    dic['total price']      = resp['sections'][list_data_loc]['widgets'][1]['data']['value']

    
    
    return dic

x = []

# url = 'https://api.divar.ir/v8/web-search/tehran/buy-apartment'
url = 'https://api.divar.ir/v8/web-search/tehran/buy-apartment?has-photo=true&sort=sort_date'
resp = requests.get(url)
resp = json.loads(resp.text)

for i in range(23):
    x.append(resp['web_widgets']['post_list'][i]['data']['token'])

s = 0
for i in x:
    print(i)
    main_dic[s] = product(i)
    with open ('divar.json','w') as l:
        json.dump(main_dic,l)
    s+=1 
    time.sleep(2)   


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