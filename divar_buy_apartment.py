
# scrape data and store all product keys and values
import json,requests
import time 
from datetime import datetime
import os.path
from unidecode import unidecode
import pandas as pd

# this is last dictionary to store
main_dic ={}

if os.path.isfile('D:\Projects\PYTHON\electrical-product-scraper\divar.json'):
    f = open('D:\Projects\PYTHON\electrical-product-scraper\divar.json')
    main_dic = json.load(f)


# current datetime
now = datetime.now()
current_date = now.date()


def product(i):
        
    # dictionary to store nested json
    dic = {}
    list_data_loc = 0
    tags_loc = 0

    # url is a variable to store desired api
    # this request response page number api of digikala , counter start from "0" but page number start from "1".beacuse of that i changed format to "counter + 1"
    url = 'https://api.divar.ir/v8/posts-v2/web/{}'.format(i)

    resp = requests.get(url,timeout=60)
    resp = json.loads(resp.text)

    for i in range(len(resp['sections'])):
        if resp['sections'][i]['section_name'] == "TAGS":
            tags_loc = i

        if resp['sections'][i]['section_name'] == "LIST_DATA":
            list_data_loc = i

    widgets_len = len(resp['sections'][list_data_loc]['widgets'])

    temp = resp['sections'][tags_loc]['widgets'][0]['data']['chip_list']['chips'][1]['action']['payload']['web_url']
    temp1 = temp.split('/')

    dic['id'] = resp['webengage']['token']
    dic['city']     = temp1[0]
    dic['category'] = temp1[1]
    dic['district'] = temp1[2]


    dic['size']     = unidecode(resp['sections'][list_data_loc]['widgets'][0]['data']['items'][0]['value'])
    dic['year of construction'] = unidecode(resp['sections'][list_data_loc]['widgets'][0]['data']['items'][1]['value'])
    dic['number of rooms']      = unidecode(resp['sections'][list_data_loc]['widgets'][0]['data']['items'][2]['value'])
    dic['floor']      = unidecode(resp['sections'][list_data_loc]['widgets'][widgets_len-3]['data']['value'].split(" ")[0])
   
    if len(resp['sections'][list_data_loc]['widgets'][widgets_len-3]['data']['value'].split(" ")) == 3:
        dic['Total floors']      = unidecode(resp['sections'][list_data_loc]['widgets'][widgets_len-3]['data']['value'].split(" ")[2])
    else:
        dic['Total floors'] = "NA"
    
    
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

    dic['date'] = str(current_date)
    dic['price per meter (Toman)']      = unidecode(resp['sections'][list_data_loc]['widgets'][2]['data']['value'].split(" ")[0])
    dic['total price (Toman)']      = unidecode(resp['sections'][list_data_loc]['widgets'][1]['data']['value'].split(" ")[0])

    
    
    return dic

a = 0
t = len(main_dic)

while True:
    
    x = []

    # url = 'https://api.divar.ir/v8/web-search/tehran/buy-apartment'
    url = 'https://api.divar.ir/v8/web-search/tehran/buy-apartment?has-photo=true&sort=sort_date'
    resp = requests.get(url,timeout=60)
    resp = json.loads(resp.text)

    for i in range(23):
        x.append(resp['web_widgets']['post_list'][i]['data']['token'])


    

    for i in x:
        print(i)
        main_dic[a+t] = product(i)
        with open ('D:\Projects\PYTHON\electrical-product-scraper\divar.json','w') as l:
            json.dump(main_dic,l)
        a+=1 
        print(a)
        
        df = pd.DataFrame.from_dict(main_dic)
        df = df.T
        df.to_csv('D:\Projects\PYTHON\electrical-product-scraper\divar.csv')

        time.sleep(2)   

    
    time.sleep(60)


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