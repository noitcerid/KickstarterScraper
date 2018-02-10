import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup
import csv

def get_pages():
    pages = []
    pages.append(requests.get('https://www.kickstarter.com/projects/1809844610/talulla-restaurant?ref=category_location&ref=discovery&term=restaurants'))
    pages.append(requests.get('https://www.kickstarter.com/projects/1099655890/the-lucky-well-a-bbq-restaurant-that-helps-the-hom?ref=discovery&term=restaurants'))

    return pages

