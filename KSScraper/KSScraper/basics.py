import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

def get_project(soup):
    '''Returns project body -> BeautifulSoup.body'''
    body = soup.body
    project = body.find('body')
    return project

def get_project_title(soup):
    '''Returns project title -> string'''
    project_name = soup.body.find_all('h2', class_='type-24 type-28-sm type-38-md navy-700 medium mb3', string = True, limit = 1)
    return project_name[0].string