import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup
import csv

def get_pages(limit = 1):
    pages = []
    #pages.append(requests.get('https://www.kickstarter.com/projects/1809844610/talulla-restaurant'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1099655890/the-lucky-well-a-bbq-restaurant-that-helps-the-hom'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1140733497/humboldt-springs-brewing-llc'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1236049502/third-coast-riviera'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1770514081/edelweiss-pastry-shop-european-pastry-in-idaho-spr'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/2091373011/emmas-tea-spot'))
    #pages.append(requests.get('https://www.kickstarter.com/projects/1839653352/terra-mare-sustainable-organic-taste-at-the-wine-c'))
    project_list = import_csv()
    count = 0
    while count < limit:
        pages.append(requests.get(project_list[count][0]))
        count += 1
    return pages

def get_soups(pages):
    soups = []
    for page in get_pages():
        soups.append(page, BeautifulSoup(page.content, 'html.parser'))

def import_csv():
    '''Returns a list of csv rows from file for iteration -> list'''
    with open('projects.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        file_data = []
        next(readCSV) #skips header row
        for row in readCSV:
            file_data.append(row)
    return file_data
