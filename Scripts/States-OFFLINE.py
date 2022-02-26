# States-OFFLINE

from bs4 import BeautifulSoup

with open('States-OFFLINE.html') as file: 
    file = file.read()

soup = BeautifulSoup(file, 'lxml')

states = soup.find_all('ul')[1]

state_names = []
state_urls = []

for state in states: 
    state_name = state.a.text.lower().replace(' ', '-')
    state_url = state.a['href']
    state_urls.append(state_url)
    state_names.append(state_name)


print(state_names)

## DONE !! 
