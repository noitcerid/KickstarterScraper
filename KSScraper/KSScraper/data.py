import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup
import csv

def get_pages():
    pages = []
    #pages.append(requests.get('https://www.kickstarter.com/projects/1809844610/talulla-restaurant'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1099655890/the-lucky-well-a-bbq-restaurant-that-helps-the-hom'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1140733497/humboldt-springs-brewing-llc'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1236049502/third-coast-riviera'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1770514081/edelweiss-pastry-shop-european-pastry-in-idaho-spr'))
    pages.append(requests.get('https://www.kickstarter.com/projects/2091373011/emmas-tea-spot'))
    return pages

def get_soups(pages):
    soups = []
    for page in get_pages():
        soups.append(page, BeautifulSoup(page.content, 'html.parser'))

def import_pages_csv(file):
    '''Returns a list of csv rows from file for iteration'''
    return None