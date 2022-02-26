# Lawyer Names
# Test City: https://attorneys.superlawyers.com/elder-law/california/los-angeles/

import requests
from bs4 import BeautifulSoup

lawyer_urls = []
next_page_urls = []


def get_lawyer_urls(url): 
    #url = 'https://attorneys.superlawyers.com/elder-law/california/los-angeles/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    # with open('Lawyer_Names-OFFLINE.html', 'w') as file: 
    #     file.write(str(soup))
    #     print('File saved for offline use.')

    try:
        lawyer_names_description = soup.find('div', id= 'poap_results')

        for link in lawyer_names_description:
            person_name = link.find('h2', class_= 'indigo_text').text.strip()
            print('Adding URL link for', person_name)
            person_link = link.find('a', class_= 'directory_profile')['href']
            lawyer_urls.append(person_link)

    except Exception as error: 
        print(error, 'Continuing...')

    try:    
        lawyer_names_no_description = soup.find('div', id= 'eoap_results')

        for link in lawyer_names_no_description:
            person_name = link.find('h2', class_= 'indigo_text').text.strip()
            print('Adding URL link for', person_name)
            person_link = link.find('a', class_= 'directory_profile')['href']
            lawyer_urls.append(person_link)

    except Exception as error:
        print(error, '...Continuing...')

    try: 
        lawyer_names_basic = soup.find('div', id= 'basic_results')

        for link in lawyer_names_basic:
            person_name = link.find('h2', class_= 'indigo_text').text.strip()
            print('Adding URL link for', person_name)
            person_link = link.find('a', class_= 'directory_profile')['href']
            lawyer_urls.append(person_link)

    except Exception as error:
        print(error, '...Continuing...')

    print('---Going to next page---')
    pagination = soup.find_all('div', class_='pagination')

    for item in pagination:
        next_page = item.find('a',  attrs={'title': 'Go to Next Page'})
        if next_page:
            next_url = next_page['href']
    
    if next_page:
        next_page_urls.append(next_url)

    else: 
        print('No more pages.')



if __name__ == '__main__':             
    get_lawyer_urls('https://attorneys.superlawyers.com/elder-law/california/los-angeles/')
    for item in next_page_urls:
        get_lawyer_urls(item)
    print('Amount of lawyers:', len(lawyer_urls))



# Los Angeles vs Other cities. 

# Run the function for every city in list. Might have to use a for loop with the function with argument. 

# 2/16/2022 - Everything might be working. Might be okay to remove else statement (print('No more pages. 1'))

# To-do: change "Adding lawyers from basic" to lawyer names. 