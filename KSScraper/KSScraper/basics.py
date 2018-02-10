import requests
import string
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

def get_project_description(soup):
    '''Returns project description'''
    description = list(soup.body.find('div', class_='full-description js-full-description responsive-media formatted-lists').find_all('p'))
    text = ''
    for item in description:
        if item.string != None:
            text += item.string
    return text

def get_project_risks(soup):
    '''Returns project risks'''
    risks =  list(soup.body.find('div', class_='mb3 mb10-sm mb3 js-risks').find_all('p'))
    text = ''
    if risks != None:
        for item in risks:
            if item.contents != None:        
                for s in item.stripped_strings:
                    cleaned_s = string.replace(str(s), '•	', '')
                    text += cleaned_s + ' '
    return text