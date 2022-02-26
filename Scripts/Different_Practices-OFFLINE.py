from bs4 import BeautifulSoup

with open('Different_Practices-OFFLINE.html') as file:
    file = file.read()

soup = BeautifulSoup(file, 'lxml')


practices_names = []
practices_names_hyphens = []
practices_urls = []

practices = soup.find_all('ul')[0]

for practice in practices: 
    practice_name = practice.find('a').text
    practices_names.append(practice_name)
    practice_link = practice.find('a')['href']
    practices_urls.append(practice_link)
    print(practice_link)