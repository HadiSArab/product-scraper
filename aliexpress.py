import time
from lxml import html
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options 
url = 'https://www.aliexpress.com/category/200000707/tops-tees.html?trafficChannel=main&catName=tops-tees&CatId=200000707&ltype=wholesale&SortType=default&page={}&isrefine=y'
xpat3 = '/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[1]/h1/text()'
xpat4 = '/html/body/div[4]/div/div/div[2]/div[2]/div/div[2]/a[{}]/div[2]/div[1]/h1/text()'
options = webdriver.ChromeOptions()
options.add_extension('D:\python\GitHub\electrical-product-scraper\Free VPN ZenMate-Best VPN for Chrome.crx')
driver = webdriver.Chrome('D:\python\GitHub\electrical-product-scraper\chromedriver.exe',options=options)  # Optional argument, if not specified will search path.
time.sleep(10)
for i in range(5):
    driver.get(url.format(i+2))
    end = driver.execute_script("return document.body.scrollHeight")
    time.sleep(10)
    x=0
    y = 0
    for x in range(10):
        x = int(y+(end/10))
        driver.execute_script(("window.scrollTo(0, {});").format(x))
        time.sleep(.5)
        y=x
        
   
    page = driver.page_source
    page = html.fromstring(page)
    for i in range (40):
        price = page.xpath(xpat3.format(i+1))
        # print(type(page))  
        print(price)
        price = page.xpath(xpat4.format(i+1))
        # print(type(page))  
        print(price)
        
        # time.sleep(30)    
    # driver.quit()
