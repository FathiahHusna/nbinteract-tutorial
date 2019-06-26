#import dataframe
import pandas as pd

#calling package URL lib
from urllib.request import urlopen as uReq
#pase HTML text
from bs4 import BeautifulSoup as soup

my_url = 'https://www.mudah.my/malaysia/cars-for-sale'

#opening up the connnection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing  
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"listing_params_container"})

filename = "df_.csv"

def subs (Mileage):
        if Mileage == "0 - 4 999":
            return Mileage.replace("0 - 4 999", "2500", 1)
        elif Mileage == "5 000 - 9 999":
            return Mileage.replace("5 000 - 9 999", "52500", 1)
        elif Mileage == "10 000 - 14 999":
            return Mileage.replace("10 000 - 14 999", "12500", 1)
        elif Mileage == "15 000 - 19 999":
            return Mileage.replace("15 000 - 19 999", "17500", 1)
        elif Mileage == "20 000 - 24 999":
            return Mileage.replace("20 000 - 24 999", "22500", 1)
        elif Mileage == "25 000 - 29 999":
            return Mileage.replace("25 000 - 29 999", "27500", 1)
        elif Mileage == "30 000 - 34 999":
            return Mileage.replace("30 000 - 34 999", "32500", 1)
        elif Mileage == "35 000 - 39 999":
            return Mileage.replace("35 000 - 39 999", "37500", 1)
        elif Mileage == "40 000 - 44 999":
            return Mileage.replace("40 000 - 44 999", "42500", 1)
        elif Mileage == "45 000 - 49 999":
            return Mileage.replace("45 000 - 49 999", "47500", 1)
        elif Mileage == "50 000 - 54 999":
            return Mileage.replace("50 000 - 54 999", "52500", 1)
        elif Mileage == "55 000 - 59 999":
            return Mileage.replace("55 000 - 59 999", "57500", 1)
        elif Mileage == "60 000 - 64 999":
            return Mileage.replace("60 000 - 64 999", "62500", 1)
        elif Mileage == "65 000 - 69 999":
            return Mileage.replace("65 000 - 69 999", "67500", 1)
        elif Mileage == "70 000 - 74 999":
            return Mileage.replace("70 000 - 74 999", "72500", 1)
        elif Mileage == "75 000 - 79 999":
            return Mileage.replace("75 000 - 79 999", "77500", 1)
        elif Mileage == "80 000 - 84 999":
            return Mileage.replace("80 000 - 84 999", "82500", 1)
        elif Mileage == "85 000 - 89 999":
            return Mileage.replace("85 000 - 89 999", "87500", 1)
        elif Mileage == "90 000 - 94 999":
            return Mileage.replace("90 000 - 94 999", "92500", 1)
        elif Mileage == "95 000 - 99 999":
            return Mileage.replace("95 000 - 99 999", "97500", 1)
        elif Mileage == "100 000 - 109 999":
            return Mileage.replace("100 000 - 109 999", "105000", 1)
        elif Mileage == "110 000 - 119 999":
            return Mileage.replace("110 000 - 119 999", "115000", 1)
        elif Mileage == "120 000 - 129 999":
            return Mileage.replace("120 000 - 129 999", "125000", 1)
        elif Mileage == "130 000 - 139 999":
            return Mileage.replace("130 000 - 139 999", "135000", 1)
        elif Mileage == "140 000 - 149 999":
            return Mileage.replace("140 000 - 149 999", "145000", 1)
        elif Mileage == "150 000 - 159 999":
            return Mileage.replace("150 000 - 159 999", "155000", 1)
        elif Mileage == "160 000 - 169 999":
            return Mileage.replace("160 000 - 169 999", "165000", 1)
        elif Mileage == "170 000 - 179 999":
            return Mileage.replace("170 000 - 179 999", "175000", 1)
        elif Mileage == "180 000 - 189 999":
            return Mileage.replace("180 000 - 189 999", "185000", 1)
        elif Mileage == "190 000 - 199 999":
            return Mileage.replace("190 000 - 199 999", "195000", 1)
        elif Mileage == "200 000 - 249 999":
            return Mileage.replace("200 000 - 249 999", "225000", 1)
        elif Mileage == "250 000 - 299 999":
            return Mileage.replace("250 000 - 299 999", "275000", 1)
        elif Mileage == "300 000 - 349 999":
            return Mileage.replace("300 000 - 349 999", "325000", 1)
        elif Mileage == "350 000 - 399 999":
            return Mileage.replace("350 000 - 399 999", "375000", 1)
        elif Mileage == "400 000 - 449 999":
            return Mileage.replace("400 000 - 449 999", "425000", 1)
        elif Mileage == "450 000 - 499 999":
            return Mileage.replace("450 000 - 499 999", "475000", 1)
        else:
            return Mileage

        
#df = pd.DataFrame(data, columns=['Name', 'Price', 'Manufactured Year', 'Mileage', 'NewMil', 'CC', 'Condition', 'Link'])


def dprice (a):
    if (' ' in a) == True:
        return ''.join(a.split())
    else:
        return a
container = []

for fathiah in containers:
    
    clink = fathiah.div.div.a["href"]
    name = fathiah.div.div.a["title"].strip()
    price = fathiah.findAll("div", {"class":"ads_price"})
    Price = price[0].text.strip()
    year = fathiah.findAll("font", {"class":"icon_label"})
    Year = year[1].text.strip()
    Mileage = year[2].text.strip()
    CC = year[3].text.strip()
    Condition = year[0].text.strip()
    
    newMil = subs(Mileage).strip()
    Price1 = Price.replace("RM", "", 1)
    nPrice = dprice(Price1)
    container.append((name, nPrice, Year, Mileage, newMil, CC, Condition, clink))
   

    
df = pd.DataFrame(container, columns = ['Name', 'Price', 'Manufactured Year', 'Mileage', 'NewMil', 'CC', 'Condition', 'Link'])
df.to_csv(filename, index=False, encoding='utf-8')
print (df)   
     
    

    
    
    
    
    
    
    
    