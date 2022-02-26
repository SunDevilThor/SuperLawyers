# Cities
# Alabama as the test state URL

import requests
from bs4 import BeautifulSoup

url = 'https://attorneys.superlawyers.com/elder-law/alabama/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

# with open('Cities-OFFLINE.html', 'w') as file: 
#     file.write(str(soup))
#     print('File saved for offline use.')

cities = soup.find('ul')

city_urls = []

for city in cities: 
    city_url = city.a['href']
    city_urls.append(city_url)


## DONE !! 