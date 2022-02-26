# Lawyer Info

# Test URL: https://profiles.superlawyers.com/california/los-angeles/lawyer/leslie-a-barnett/b972073f-95a2-4f0e-9702-f53f605f790c.html

import requests
from bs4 import BeautifulSoup

url = 'https://profiles.superlawyers.com/california/los-angeles/lawyer/leslie-a-barnett/b972073f-95a2-4f0e-9702-f53f605f790c.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

# with open('Lawyer_Info-OFFLINE.html', 'w') as file: 
#     file.write(str(soup))
#     print('File saved for offline use.')

attorneys_list = []

# lawyer_name = soup.find('h2', id='lawyer_name').text
# try: 
#     firm_name = soup.find('a', id='firm_profile_page').text
# except Exception as error: 
#     print('...No firm listed.')
#     firm_name = ''
# try: 
#     address = soup.find('div', id= 'firm_map_info').text
# except Exception as error: 
#     print('...No address listed.')
#     address = ''
# try: 
#     lawyer_website = soup.find_all('div', class_= 'contact_info_blocks')[1].text.replace('Visit:', '').strip()
# except Exception as error: 
#     print('...No website listed.')
#     lawyer_website = ''
# try: 
#     phone_number = soup.find_all('div', class_= 'contact_info_blocks')[2].text.replace('Phone:', '').strip()
# except Exception as error: 
#     print('...No phone number listed.')
#     phone_number = ''
# try: 
#     fax_number = soup.find_all('div', class_= 'contact_info_blocks')[3].text.replace('Fax:', '').strip()
# except Exception as error: 
#     print('...No fax number listed.')
#     fax_number = ''

try: 
    education = soup.find('div', id='law_school').text.replace('Education:', '').strip()
    print(education)
except Exception as error: 
    print(error, '...No education listed.')
    education = ''

try: 
    law_practices = soup.find('div', id='practice_areas').text.replace('Practice Areas:', '').strip()
    print(law_practices)
except Exception as error: 
    print(error, '...No law practices listed.')
    law_practices = ''


# lawyer = {
#     'lawyer_name': lawyer_name,
#     'firm_name': firm_name,
#     'lawyer_website': lawyer_website,
#     'phone_number': phone_number, 
#     'fax_number': fax_number,
#     'education': education,
#     'address': address,
#     'law_practices': law_practices,
# }


lawyer = {
    'education': education,
    'law_practices': law_practices,
}

print(lawyer)
