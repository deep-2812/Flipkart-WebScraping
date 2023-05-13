#About this project:
# In this project, we will be scraping the data of apple products from flipkart

import requests
from bs4 import BeautifulSoup
import pandas as pd

l = []
for i in range(1,59):
    url = f'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&as-pos=3&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=dadd0e7c-60f6-4d8c-9889-e405309a7cf2&as-backfill=on&page={i}'

    #Requesting for data
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, "lxml")
    boxes = soup.find_all('a', '_1fQZEK')
    for box in boxes:
        laptop_dict = {}
        name = box.find('div', '_4rR01T').get_text()
        retail_price = box.find('div', '_30jeq3 _1_WHN1').get_text()
        try:
            mrp = box.find('div', '_3I9_wc _27UcVY').get_text()
        except AttributeError:
            mrp = retail_price
        try:
            rating = box.find('div', '_3LWZlK').get_text()
        except AttributeError:
            laptop_dict["Rating"] = ""
        laptop_dict["Brand"] = name.split(" ")[0]
        laptop_dict["Name"] = name
        laptop_dict["Retail Price"] = retail_price
        laptop_dict["MRP"] = mrp
        laptop_dict["Rating"] = rating
        l.append(laptop_dict)
df = pd.json_normalize(l)
df.to_excel("D:\Documents\Projects\Laptop.xlsx")
