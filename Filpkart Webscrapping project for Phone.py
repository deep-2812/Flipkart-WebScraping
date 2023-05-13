# This is practice webscrapping project, we are going to fetch phone's data from flipkart
#importing necessary libraries

import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
l = []
for i in range(1, 25):
    url = f'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}'

    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'lxml')
    boxes = soup.find_all('a', '_1fQZEK')
    for box in boxes:
        #Distionary:
        phone_data = {}
        phone_data['Name'] = box.find('div', '_4rR01T').get_text()
        phone_data["Price"] = box.find('div', '_30jeq3 _1_WHN1').get_text()
        try:
            phone_data["Rating"] = box.find('div', "_3LWZlK").get_text()
        except AttributeError:
            phone_data["Rating"] =  ""
        phone_data["Brand"] = phone_data['Name'].split(' ')[0]
        #list:
        l.append(phone_data)
df = pd.json_normalize(l)
df.to_excel("D:\Documents\Projects\Phone.xlsx")