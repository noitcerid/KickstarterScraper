import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

def get_backer_cities(soup):
    '''Returns a list of all backer cities'''
    locations_cities = soup.body.find('div', class_='community-section__locations_cities')
    locations_cities_sub = locations_cities.find('div', class_='location-list js-locations-cities')
    locations_cities_sub_items = list(locations_cities_sub.find_all('div', class_='location-list__item js-location-item'))
    return locations

def get_top_backer_city(backer_cities):
    city_list = ' '.join(backer_cities)
    return str(city_list)
