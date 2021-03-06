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
        lawyer_names_description = soup.find_all(id='poap_results')    ### WORKING ### 

        for section in lawyer_names_description:
            individual = section.find_all('div', class_="poap serp-container lawyer")
            for person in individual: 
                try: 
                    person_name = person.find('h2', class_='indigo_text').text.strip()
                    person_link = person.find('a', class_='directory_profile')['href']

                    if person_link not in lawyer_urls:
                        print('Adding URL link for', person_name)
                        lawyer_urls.append(person_link)

                except: 
                    pass
                    print('NOTHING HERE')         ### WORKING ### 

    except Exception as error:
        pass

    try: 
        lawyer_names_no_description = soup.find_all(id='eoap_results')

        for section in lawyer_names_no_description:
            individual = section.find_all('div', class_="eoap serp-container lawyer")
            for person in individual: 
                try: 
                    person_name = person.find('h2', class_='indigo_text').text.strip()
                    person_link = person.find('a', class_='directory_profile')['href']

                    if person_link not in lawyer_urls:
                        print('Adding URL link for', person_name)
                        lawyer_urls.append(person_link)

                except: 
                    pass
                    print('NOTHING HERE')   
            
    except Exception as error:
        pass

    try: 
        lawyer_names_basic = soup.find_all(id='basic_results')

        for section in lawyer_names_basic:
            individual = section.find_all('div', class_="basic serp-container lawyer")
            for person in individual: 
                try: 
                    person_name = person.find('h2', class_='indigo_text').text.strip()
                    person_link = person.find('a', class_='directory_profile')['href']

                    if person_link not in lawyer_urls:
                        print('Adding URL link for', person_name)
                        lawyer_urls.append(person_link)

                except: 
                    pass
                    print('NOTHING HERE')  

    except Exception as error:
        pass

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
    get_lawyer_urls('https://attorneys.superlawyers.com/personal-injury-general/illinois/palatine/')
    for item in next_page_urls:
        get_lawyer_urls(item)
    print('Amount of lawyers:', len(lawyer_urls))
    print(next_page_urls)
    print(lawyer_urls)