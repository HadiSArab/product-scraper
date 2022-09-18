import time
from lxml import html
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options 
url = 'https://www.basalam.com/'
xpat = '/html/body/div[3]/div/div/div[2]/div[2]/div/div[2]/a[4]/div[2]/div[1]/h1/text()'
options = webdriver.ChromeOptions()
options.add_extension('D:\python\GitHub\electrical-product-scraper\Free VPN ZenMate-Best VPN for Chrome.crx')
driver = webdriver.Chrome('D:\python\GitHub\electrical-product-scraper\chromedriver.exe',options=options)  # Optional argument, if not specified will search path.

driver.get(url)
end = driver.execute_script("return document.body.scrollHeight")
print(end)
print(type(end))
print(int(end))
x=0
for i in range(5):
    x += end/5
    driver.execute_script(("window.scrollTo(0, {});").format(x))
    time.sleep(.3)
time.sleep(10)