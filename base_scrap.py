# Import required modules
from lxml import html
import requests,json


# Request the page
url = 'https://www.aliexpress.com/category/100003070/men-clothing.html'
page = requests.get(url)

# Parsing the page
# (We need to use page.content rather than 
# page.text because html.fromstring implicitly
# expects bytes as input.)
page = html.fromstring(page.content)  

x = page.xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[2]/div[2]/div[1]/h1/text()')
for i in x:
    print(i)
