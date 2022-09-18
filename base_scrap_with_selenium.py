import time
from lxml import html
from selenium import webdriver
import requests


driver = webdriver.Chrome('D:\python\GitHub\electrical-product-scraper\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://torob.com/browse/94/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-mobile/')
page = driver.page_source
page = html.fromstring(page)
price = page.xpath("/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/a/div/div/div[2]/div[2]/text()")

# time.sleep(5)
# print(type(page))
print(price)
driver.quit()

