from re import I
import requests
from bs4 import BeautifulSoup

lawyer_urls = []
lawyer_urls

def get_names(url): 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

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





if __name__ == '__main__':
    get_names('https://attorneys.superlawyers.com/personal-injury-general/illinois/palatine/page15/')
    print('Amount of lawyers:')
    print(len(lawyer_urls))