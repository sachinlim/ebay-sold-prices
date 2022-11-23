import requests
from bs4 import BeautifulSoup
import statistics


# take user input for search term
def user_input():
    while True:
        try:
            item = input('Enter the item to search: ')
            formatted_item = item.replace(' ', '+')

            if item != '':
                return formatted_item
        except ValueError:
            print('Please enter an item to search for!')


def website_data(search):
    # URL contains search filters: used items and sold listings
    url = f'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw={search}' \
          f'&_in_kw=1&_ex_kw=&_sacat=0&LH_Sold=1&_udlo=&_udhi=&LH_ItemCondition=4&_samilow=&_samihi=&_sadis=15' \
          f'&_stpos=M300AA&_sargn=-1%26saslc%3D1&_salic=3&_sop=12&_dmd=1&_ipg=60&LH_Complete=1&rt=nc&LH_PrefLoc=1'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_data(soup):
    products = []
    results = soup.find('div', {'class': 'srp-river-results clearfix'}).find_all('li', {'class': 's-item '
                                                                                                 's-item__pl-on-bottom'})
    for item in results:
        price = item.find('span', class_='s-item__price').text.replace('£', '').replace(',', '')

        if 'to' not in price:
            price = float(price)
            products.append(price)

    return products


def calculate_averages(products):
    mean = round(statistics.mean(products), 2)
    median = round(statistics.median(products), 2)
    mode = round(statistics.mode(products), 2)

    return mean, median, mode


search_term = user_input()
soup = website_data(search_term)
my_list = get_data(soup)

mean, median, mode = calculate_averages(my_list)
print(f'Total results: {str(len(my_list))}')
print('')
print(f'The average sold price: £{str(mean)}')
print(f'The median price is: £{str(median)}')
print(f'The mode is: £{str(mode)}')
