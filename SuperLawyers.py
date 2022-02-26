# Attorneys - SuperLawyers 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys


state_names = []
state_names_hyphens = []
state_urls = []
city_names = []
city_urls = []
practices_names = []
practices_names_hyphens = []
practices_urls = []
lawyer_urls = []
next_page_urls = []
attorneys_list = []


def get_state_names(): 
    """Gets the name of each state in the USA"""

    url = 'https://attorneys.superlawyers.com/states/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    states = soup.find_all('ul')[0]

    for state in states: 
        state_name = state.find('a').text
        state_names.append(state_name)
        state_name_hyphen = state.find('a').text.lower().replace(' ', '-')
        state_names_hyphens.append(state_name_hyphen)

    print('Getting state names and URLs...')

def get_state_urls():
    """Gets the URL for each state in the USA."""

    url = 'https://attorneys.superlawyers.com/states/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    states = soup.find_all('ul')[0]

    for state in states: 
        state_url = state.a['href']
        state_urls.append(state_url)


def get_city_urls():
    """Gets the URL for each city."""

    for state in state_names_hyphens:
        print('Getting city URLs for:', state.upper().replace('-', ' '))
        url = f'https://attorneys.superlawyers.com/{state}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
        response = session.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        cities = soup.find('ul')

        for city in cities: 
            city_name = city.a.text
            city_names.append(city_name)
            city_url = city.a['href']
            city_urls.append(city_url)

def get_practices():
    """Gets all the different types of practices from lawyers."""

    url = 'https://attorneys.superlawyers.com/practice/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    practices = soup.find_all('ul')[0]

    for practice in practices: 
        practice_name = practice.find('a').text
        practices_names.append(practice_name)
        practice_link = practice.find('a')['href']
        practices_urls.append(practice_link)


def get_lawyer_urls(main_url): 
    """Gets the URL for each lawyer listed."""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    response = session.get(main_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    try:
        lawyer_names_description = soup.find('div', id= 'poap_results')

        for link in lawyer_names_description:
            person_name = link.find('h2', class_= 'indigo_text').text.strip()
            person_link = link.find('a', class_= 'directory_profile')['href']
            if person_link not in lawyer_urls:
                print('Adding URL link for', person_name)
                lawyer_urls.append(person_link)

    except Exception as error: 
        pass

    try:    
        lawyer_names_no_description = soup.find('div', id= 'eoap_results')

        for link in lawyer_names_no_description:
            person_name = link.find('h2', class_= 'indigo_text').text.strip()
            person_link = link.find('a', class_= 'directory_profile')['href']
            if person_link not in lawyer_urls:
                print('Adding URL link for', person_name)
                lawyer_urls.append(person_link)

    except Exception as error:
        pass

    try: 
        lawyer_names_basic = soup.find('div', id= 'basic_results')

        for link in lawyer_names_basic:
            person_name = link.find('h2', class_= 'indigo_text').text.strip()
            person_link = link.find('a', class_= 'directory_profile')['href']
            if person_link not in lawyer_urls:
                print('Adding URL link for', person_name)
                lawyer_urls.append(person_link)

    except Exception as error:
        pass

    print('---Going to next page---')

    try: 
        pagination = soup.find_all('div', class_='pagination')
    except: 
        print('No more pages. Test 1')

    if pagination: 
        for item in pagination:
            next_page = item.find('a',  attrs={'title': 'Go to Next Page'})
            if next_page:
                next_url = next_page['href']
        
        if next_page:
            next_page_urls.append(next_url)

        else: 
            print('No more pages.')


def lawyer_info(url):
    """Gets the contact information for each lawyer."""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml') 

    lawyer_name = soup.find('h2', id='lawyer_name').text
    print('Scraping data from:', lawyer_name)
    
    try: 
        firm_name = soup.find('a', id='firm_profile_page').text
    except Exception as error: 
        print('...No firm listed.')
        firm_name = ''
    try: 
        address = soup.find('div', id= 'firm_map_info').text
    except Exception as error: 
        print('...No address listed.')
        address = ''
    try: 
        lawyer_website = soup.find_all('div', class_= 'contact_info_blocks')[1].text.replace('Visit:', '').strip()
    except Exception as error: 
        print('...No website listed.')
        lawyer_website = ''
    try: 
        phone_number = soup.find_all('div', class_= 'contact_info_blocks')[2].text.replace('Phone:', '').strip()
    except Exception as error: 
        print('...No phone number listed.')
        phone_number = ''
    try: 
        fax_number = soup.find_all('div', class_= 'contact_info_blocks')[3].text.replace('Fax:', '').strip()
    except Exception as error: 
        print('...No fax number listed.')
        fax_number = ''

    try: 
        education = soup.find('div', id='law_school').text.replace('Education:', '').strip()
    except Exception as error: 
        print('...No education listed.')
        education = ''

    try: 
        law_practices = soup.find('div', id='practice_areas').text.replace('Practice Areas:', '').strip()
    except Exception as error: 
        print('...No law practices listed.')
        law_practices = ''

    lawyer = {
        'lawyer_name': lawyer_name,
        'firm_name': firm_name,
        'lawyer_website': lawyer_website,
        'phone_number': phone_number, 
        'fax_number': fax_number,
        'education': education,
        'address': address,
        'law_practices': law_practices,
    }

    attorneys_list.append(lawyer)


def output(): 
    df = pd.DataFrame(attorneys_list)
    df.to_csv(f'Attorney_Info_{user_selection}_{user_city}.csv')
    print('Saved information to CSV file.')



if __name__ == '__main__':
    session = requests.Session()
    get_state_names()
    get_state_urls()
    print('\nAmount of states:', len(state_urls)-1)  # Should be 50
    get_city_urls()
    print('\nAmount of cities:', len(city_urls)-1)  # 8120 Cities 
    get_practices()
    print('\nAmount of practices listed:', len(practices_names)-1) 

    while True: 
        user_selection = input('\nWhat practice are you interested? (Press "q" to Quit).\n')
        if user_selection in practices_names:
            user_selection = user_selection.lower().replace(' ', '-').replace('&', 'and')
            user_city = input('\nWhat city are you in?\n')
            if user_city in city_names: 
                user_city = user_city.lower().replace(' ', '-')
                user_state = input('\nWhat state you are in?\n')
                if user_state in state_names:
                    user_state = user_state.lower().replace(' ', '-')

                    main_url = f'https://attorneys.superlawyers.com/{user_selection}/{user_state}/{user_city}'
                    print('Scraping information from:', main_url)

                    print('Getting information from this location...')
                    get_lawyer_urls(main_url)

                    if len(lawyer_urls) != 0: 
                        print('\nThere are ' + str(len(lawyer_urls)) + ' lawyers in your area for', user_selection.title().replace('-', ' ').replace('and', '&'))
                    else: 
                        print('There are no lawyers in this area for ', user_selection.title().replace('-', ' ').replace('and', '&'))

                    for item in next_page_urls:
                        print('\nGetting information from:', item)
                        get_lawyer_urls(item)
                    for url in lawyer_urls:
                        lawyer_info(url)

                    print('\nAmount of lawyers found:', len(lawyer_urls))
                    output()
                    print('---- FINISHED ---- ')

                    sys.exit()

                else: 
                    print('Error. Enter in a valid state name.')

            else: 
                print('Sorry, that city is either not found or does not have any practicing lawyers servicing it.')

        else:
            print('Error. Select an applicable practice from the ones listed.')

        if user_selection == 'q':
            print('Exiting...')
            sys.exit()
                    



# Fix While loop to loop over current question and not start over from beginning. 

# Make a separate list for lawyer names

# Time the script

