import requests
import string
#from pip._vendor import requests
from bs4 import BeautifulSoup

def get_backer_cities(page):
    '''Returns a list of all backer cities'''
    response = requests.get(page.url + '/community')
    soup = BeautifulSoup(response.content, 'html.parser')
    city_info = []
    locations_cities = soup.find('div', class_='location-list js-locations-cities')
    
    #Cities may not exist if no backers supported (or didn't list a location). Check to see if any cities were returned before processing, otherwise return an empty list
    if locations_cities != None:
        locations_cities_sub = list(locations_cities.find_all('div', 'location-list__item js-location-item')) 
        locations_cities_sub_items = [] 
        for city in locations_cities_sub:
            for line in city.stripped_strings:
                city_info.append(line)
    return city_info

def get_top_backer_city(backer_cities):
    if len(backer_cities) > 0:
        return str(backer_cities[0])
    else:
        return str('N/A')

def get_top_backer_city_backers_count(backer_cities):
    count = 0
    if len(backer_cities) > 0:
        count = backer_cities[2].replace(' backers', '').replace(' backer', '')
    return int(count)
