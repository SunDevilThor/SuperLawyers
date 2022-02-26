# Lawyer_Info-OFFLINE

from bs4 import BeautifulSoup

with open('Lawyer_Info-OFFLINE.html') as file: 
    file = file.read()

soup = BeautifulSoup(file, 'lxml')


attorneys_list = []

lawyer_name = soup.find('h2', id='lawyer_name').text
try: 
    firm_name = soup.find('a', id='firm_profile_page').text
except Exception as error: 
    print(error, '...No firm listed.')
    firm_name = ''
try: 
    address = soup.find('div', id= 'firm_map_info').text
except Exception as error: 
    print(error, '...No address listed.')
    address = ''
try: 
    lawyer_website = soup.find_all('div', class_= 'contact_info_blocks')[1].text.replace('Visit:', '').strip()
except Exception as error: 
    print(error, '...No website listed.')
    lawyer_website = ''
try: 
    phone_number = soup.find_all('div', class_= 'contact_info_blocks')[2].text.replace('Phone:', '').strip()
except Exception as error: 
    print(error, '...No phone number listed.')
    phone_number = ''
try: 
    fax_number = soup.find_all('div', class_= 'contact_info_blocks')[3].text.replace('Fax:', '').strip()
except Exception as error: 
    print(error, '...No fax number listed.')
    fax_number = ''


lawyer = {
    'lawyer_name': lawyer_name,
    'firm_name': firm_name,
    'lawyer_website': lawyer_website,
    'phone_number': phone_number, 
    'fax_number': fax_number,
}

print(lawyer)


# Notes: 
# Address 


# To-Do: WORK ON ADDRESS
# Output: 1631 Beverly Blvd.1st FloorLos Angeles, CA 90026