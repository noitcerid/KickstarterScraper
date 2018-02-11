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
    #Default project title format, but apparently there is a multitude of options, so will need more verbose work here
    #project_name = soup.body.find_all('h2', class_='type-24 type-28-sm type-38-md navy-700 medium mb3', string = True, limit = 1)
    project_name = ''
    project_name = soup.title.string.replace(' —Kickstarter', '')
    #return project_name[0].string
    return project_name

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
    ######## TODO: Need to evaluate cleaning text further as it's calculating high when bullets (and possible other formatting?) is used
    risks =  list(soup.body.find('div', class_='mb3 mb10-sm mb3 js-risks').find_all('p'))
    text = ''
    if risks != None:
        for item in risks:
            if item.contents != None:        
                for s in item.stripped_strings:
                    text += s + ' '
    return text

def get_project_updates_count(soup):
    '''Returns project updates -> list'''
    updates = list(soup.body.find('a', class_='js-load-project-content js-load-project-updates mx3 project-nav__link--updates tabbed-nav__link type-14'))
    #print(str(updates[1].string))
    return int(updates[1].string)

def get_project_comments_count(soup):
    '''Returns project comments count -> int'''
    comments = soup.body.find('a', class_='js-load-project-comments js-load-project-content mx3 project-nav__link--comments tabbed-nav__link type-14').find('span').find('data').string
    return int(comments)