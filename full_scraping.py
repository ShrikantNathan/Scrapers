from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd


class ApartmentsPriceFloorPlanScraper:
    def __init__(self):
        self.citadel_url = requests.get('https://www.apartments.com/citadel-at-tech-ridge-austin-tx/mp90ncj/', headers={'User-Agent': 'Mozilla'})
        self.tech_url = requests.get('https://www.apartments.com/tech-junction-austin-tx/4y51vvk/', headers={'User-Agent': 'Mozilla'})
        self.vineyard_url = requests.get('https://www.apartments.com/vineyard-pflugerville-tx/6se6hkv/', headers={'User-Agent': 'Mozilla'})
        # creating containers for citadel floor plans
        self.citadel_bedrooms_list = list()
        self.citadel_prices = list()
        self.citadel_sqft_list = list()
        # creating containers for tech_junction floor plans
        self.tech_junction_bedrooms_list = list()
        self.tech_junction_prices = list()
        self.tech_junction_sqft_list = list()
        # creating containers for vineyard floor plans
        self.vineyard_bedrooms_list = list()
        self.vineyard_prices = list()
        self.vineyard_sqft_list = list()

        self.citadel_soup = bs4(self.citadel_url.content, 'html.parser')
        self.tech_junction_soup = bs4(self.tech_url.content, 'html.parser')
        self.vineyard_soup = bs4(self.vineyard_url.content, 'html.parser')

    def get_floor_plans_for_citadel_ridge(self):
        for prices in self.citadel_soup.find_all('div', {'class': 'pricingColumn column'}):
            self.citadel_prices.append(str(prices.get_text()).strip().replace(' ', '').split()[-1].split('$')[-1])
        # for i in range(len(self.citadel_prices)):
        #     if 'CallforRent' in self.citadel_prices:
        #         self.citadel_prices.remove('CallforRent')

        for sqft_values in self.citadel_soup.find_all('div', 'sqftColumn column'):
            self.citadel_sqft_list.append(str(sqft_values.get_text()).strip().replace(' ', '').split()[-1])

        for bed_values in self.citadel_soup.find_all('h4', {'class': 'detailsLabel'}):
            self.citadel_bedrooms_list.append(str(bed_values.get_text()).strip().replace(' ', '').split()[0].split(',')[0][0])
        print(len(self.citadel_prices), len(self.citadel_sqft_list), len(self.citadel_bedrooms_list))
        df = pd.DataFrame({'Prices': self.citadel_prices, 'Sqft': self.citadel_sqft_list})
        df.to_excel('citadel_scraped.xlsx', sheet_name='sheet1', index=False)

    def get_floor_plans_for_tech_junction(self):
        for prices in self.tech_junction_soup.find_all('div', {'class': 'pricingColumn column'}):
            self.tech_junction_prices.append(str(prices.get_text()).strip().replace(' ', '').split()[-1].split('$')[-1])
        for sqft_values in self.tech_junction_soup.find_all('div', 'sqftColumn column'):
            self.tech_junction_sqft_list.append(str(sqft_values.get_text()).strip().replace(' ', '').split()[-1])
        print(len(self.tech_junction_prices), len(self.tech_junction_sqft_list))
        for bed_values in self.tech_junction_soup.find_all('h4', {'class': 'detailsLabel'}):
            self.tech_junction_bedrooms_list.append(str(bed_values.get_text()).strip().replace(' ', '').split()[0].split(',')[0][0])
        print(len(self.tech_junction_bedrooms_list))
        df = pd.DataFrame({'Prices': self.tech_junction_prices, 'Sqft': self.tech_junction_sqft_list})
        # df2 = pd.DataFrame({'Beds': self.citadel_bedrooms_list})
        # df = df.append()
        df.to_excel('tech_junction_scraped.xlsx', sheet_name='sheet1', index=False)

    def get_floor_plans_for_vineyard(self):
        for prices in self.vineyard_soup.find_all('div', {'class': 'pricingColumn column'}):
            self.vineyard_prices.append(str(prices.get_text()).strip().replace(' ', '').split()[-1].split('$')[-1])
        for sqft_values in self.vineyard_soup.find_all('div', 'sqftColumn column'):
            self.vineyard_sqft_list.append(str(sqft_values.get_text()).strip().replace(' ', '').split()[-1])
        print(len(self.vineyard_prices), len(self.vineyard_sqft_list))
        for bed_values in self.vineyard_soup.find_all('h4', {'class': 'detailsLabel'}):
            self.vineyard_bedrooms_list.append(str(bed_values.get_text()).strip().replace(' ', '').split()[0].split(',')[0][0])
        print(len(self.vineyard_bedrooms_list))

        df = pd.DataFrame({'Prices': self.vineyard_prices, 'Sqft': self.vineyard_sqft_list})
        df2 = pd.DataFrame({'Beds': self.vineyard_bedrooms_list})
        df = df.append(df2, ignore_index=True)
        df.to_excel('vineyard_scraped.xlsx', sheet_name='sheet1', index=False)


scraper = ApartmentsPriceFloorPlanScraper()
scraper.get_floor_plans_for_citadel_ridge()
scraper.get_floor_plans_for_tech_junction()
scraper.get_floor_plans_for_vineyard()