import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

def get_backer_cities(page):
    '''Returns a list of all backer cities'''
    response = requests.get(page.url + '/community')
    soup = BeautifulSoup(response.content, 'html.parser')
    locations_cities = soup.find('div', class_='location-list js-locations-cities')
    locations_cities_sub = list(locations_cities.find_all('div', 'location-list__item js-location-item')) 
    locations_cities_sub_items = [] 
    city_info = []
    for city in locations_cities_sub:
        for line in city.stripped_strings:
            city_info.append(line)
    return city_info

def get_top_backer_city(backer_cities):
    return str(backer_cities[0])
