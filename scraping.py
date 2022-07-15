from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.apartments.com/sur512-austin-tx/hmbl3h3/'
headers = {"User-Agent": 'Mozilla'}             # Search 'my user agent' on Google and paste it completely inside the curly braces

apartment_url = requests.get(URL, headers=headers)
soup = bs(apartment_url.content, 'html.parser')
txt = soup.find_all("h3", {"class": "modelLabel"})
rents = soup.find_all("span", {"class": "rentLabel"})
specifications = soup.find_all('span', {'class': 'detailsTextWrapper'})
nested_spans = soup.find_all('span', {'class': 'detailsTextWrapper'})
nested_texts = [span.get_text().strip().replace(' ', '') for span in nested_spans if 'Available Soon' not in span.get_text()]
# print(nested_texts)
all_headings, all_rents, nested_desc = [], [], []

for word in txt:
    modelName = word.get_text()
    all_headings.append(modelName.strip().replace(' ', '').split()[0])
    # print(modelName.strip().split(' ')[0])

for word in rents:
    rentVal = word.get_text()
    all_rents.append(rentVal.strip().replace(' ', '').split()[0])
    # print(rentVal)

    for desc in specifications:
        if 'Available Soon' not in desc.get_text():
            descVal = desc.get_text()
            nested_desc.append(descVal.strip().replace(' ', ''))
            # print(descVal.strip().replace(' ', ''), end='\n')

mapped_data = list()
for heading in all_headings:
    for rent in all_rents:
        for desc in nested_desc:
            mapped_data.append(list((heading, rent, desc)))

# mapped_data_2 = list(map(lambda x, y, z: f'{x}: {zip(y, z)}', [all_headings, all_rents, nested_desc]))
# print(mapped_data_2)

# print('mapped_data', mapped_data)
print(all_headings)
print(all_rents)
print(nested_desc)
