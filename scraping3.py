from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

URL_3 = "https://citadelattechridge.com/floorplans/"
URL_4 = "https://lakelinecrossing.securecafe.com/onlineleasing/lakeline-crossing0/oleapplication.aspx?stepname=Apartments&myOlePropertyId=1314356&floorPlans=3544260"

base_url = requests.get(URL_4, headers={"User-Agent": "Mozilla"})
soup = bs4(base_url.content, 'html.parser')
prices_list, sqft_list = list(), list()

floor_plans = soup.find_all("div", {"class": "block"})
for rent in floor_plans:
    min_sqft = rent.get_text()
    sqft = soup.find_all("td", {"data-label": "Sq. Ft."})
    for value in sqft:
        sqft_list.append(value.get_text())
        # print(value.get_text())

for price in floor_plans:
    min_price = soup.find_all("td", {"data-label": "Rent"})
    for value in min_price:
        prices_list.append(str(value.get_text()).split('-')[0])
        # print(str(value.get_text()).split('-')[0])

DF = pd.DataFrame({"Sqft": sqft_list, "Price": prices_list})
DF.to_excel("scraped_data.xlsx", sheet_name='sheet1', index=False)
# DF.append()