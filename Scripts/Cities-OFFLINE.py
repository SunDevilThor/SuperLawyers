# Cities-OFFLINE

from bs4 import BeautifulSoup

with open('Cities-OFFLINE.html') as file: 
    file = file.read()

soup = BeautifulSoup(file, 'lxml')

cities = soup.find('ul')

city_urls = []

for city in cities: 
    city_url = city.a['href']
    city_urls.append(city_url)

print(city_urls)

## DONE !! 