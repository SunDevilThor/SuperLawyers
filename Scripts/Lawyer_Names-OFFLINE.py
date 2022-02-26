# Lawyer_Names-OFFLINE

from bs4 import BeautifulSoup


lawyer_urls = []


with open('Lawyer_Names-OFFLINE.html') as file: 
    file = file.read()

soup = BeautifulSoup(file, 'lxml')

lawyer_names_description = soup.find('div', id= 'poap_results')

for link in lawyer_names_description:
    person_name = link.find('h2', class_= 'indigo_text').text.strip()
    print(person_name)
    person_link = link.find('a', class_= 'directory_profile')['href']
    lawyer_urls.append(person_link)

lawyer_names_no_description = soup.find('div', id= 'eoap_results')

for link in lawyer_names_no_description:
    person_name = link.find('h2', class_= 'indigo_text').text.strip()
    print(person_name)
    person_link = link.find('a', class_= 'directory_profile')['href']
    lawyer_urls.append(person_link)

lawyer_names_basic = soup.find('div', id= 'basic_results')

for link in lawyer_names_basic:
    person_name = link.find('h2', class_= 'indigo_text').text.strip()
    print(person_name)
    person_link = link.find('a', class_= 'directory_profile')['href']
    lawyer_urls.append(person_link)


print(len(lawyer_urls))



'''

# pagination = soup.find_all('div', class_='pagination')

# if pagination: 

print(len(lawyer_urls)-1)
print('Scraped all data so far.')

next_page = soup.find('a',  attrs={'title': 'Go to Next Page'})

if next_page: 
    print('Found Next Page')



<a href="https://attorneys.superlawyers.com/elder-law/california/los-angeles/page4/" rel="next nofollow" title="Go to Next Page">Next&nbsp;»</a>

<a href="https://attorneys.superlawyers.com/elder-law/california/los-angeles/" title="Go to First Page">«&nbsp;First</a>

<a href="https://attorneys.superlawyers.com/elder-law/california/los-angeles/page3/" rel="prev nofollow" title="Go to Previous Page">«&nbsp;Previous</a>

'''


# To-Do: Work on pagination