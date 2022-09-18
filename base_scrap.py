# Import required modules
from lxml import html
import requests,json


# Request the page
url = 'https://torob.com/browse/94/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-mobile/'
page = requests.get(url)

# Parsing the page
# (We need to use page.content rather than 
# page.text because html.fromstring implicitly
# expects bytes as input.)
page = html.fromstring(page.content)  

x = page.xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/a/div/div/div[2]/div[2]/text()')
for i in x:
    print(i)
