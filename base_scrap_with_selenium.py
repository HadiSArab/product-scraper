import time
from lxml import html
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_extension('D:\python\GitHub\electrical-product-scraper\Free VPN ZenMate-Best VPN for Chrome.crx')

driver = webdriver.Chrome('D:\python\GitHub\electrical-product-scraper\chromedriver.exe',options=options)  # Optional argument, if not specified will search path.

driver.get('https://www.aliexpress.com/category/200000707/tops-tees.html?trafficChannel=main&catName=tops-tees&CatId=200000707&ltype=wholesale&SortType=default&page=2&isrefine=y')
time.sleep(10)
page = driver.page_source
page = html.fromstring(page)
price = page.xpath("/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[2]/div[2]/div[1]/h1/text()")


# print(type(page))
print(price)
# driver.quit()
