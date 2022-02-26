import requests
from bs4 import BeautifulSoup

url = 'https://attorneys.superlawyers.com/practice/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

practices = soup.find_all('div', id='practice_areas_container')


with open('Different_Practices-OFFLINE.html', 'w') as file: 
    file = file.write(str(soup))
    print('Saved for offline parsing.')
