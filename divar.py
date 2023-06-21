import pandas as pd
from unidecode import unidecode
import json,os.path

if os.path.isfile('D:\Projects\PYTHON\electrical-product-scraper\divar.json'):
    f = open('D:\Projects\PYTHON\electrical-product-scraper\divar.json')
    main_dic = json.load(f)


df = pd.DataFrame.from_dict(main_dic)
df = df.T
df.to_csv('D:\Projects\PYTHON\electrical-product-scraper\divar.csv')