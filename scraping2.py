from bs4 import BeautifulSoup as bs4
import requests, pprint
import pandas as pd

prices_list, sqft_list = list(), list()
URL = "https://www.lantower.com/properties/tx/pflugerville/ambrosio/plans/"
URL_2 = "https://www.livetechjunction.com/austin/tech-junction/conventional/"

base_url = requests.get(URL, headers={"User-Agent": "Mozilla"})
soup = bs4(base_url.content, 'html.parser')

apartment_detail_slots_top = soup.find_all("div", {"class": "layout--top"})
apartment_detail_slots_bottom = soup.find_all("div", {"class": "layout--bottom"})
for elem in apartment_detail_slots_top:
    price = elem.get_text()
    # print(str(price).strip().replace(' ', '').split()[1])
    prices_list.append(str(price).strip().replace(' ', '').split()[1])
# print(pprint.pprint(prices))
for elem in apartment_detail_slots_bottom:
    sqft = elem.get_text()
    sqft_list.append(str(sqft).strip().replace(' ', '').split()[-1])

second_url = requests.get(URL_2, headers={"User-Agent": "Mozilla"})
soup2 = bs4(second_url.content, 'html.parser')

floor_details = soup2.find_all("div", {"class": "fp-col-wrapper"})
for floor_detail in floor_details:
    rent = floor_detail.get_text()
    sqft_list.append(str(rent).strip().replace(' ', '').split('$')[1].split('D')[0].split('/')[0])
    # print(str(rent).strip().replace(' ', '').split('$')[1].split('D')[0])

DF = pd.read_excel("./scraped_data.xlsx")