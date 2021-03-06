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
    project_name = ''
    project_name = soup.title.string.replace(' —Kickstarter', '')
    return project_name

def get_project_description(soup):
    '''Returns project description'''
    description = list(soup.body.find('div', class_='full-description js-full-description responsive-media formatted-lists').find_all('p'))
    text = ''
    for item in description:
        if item.string != None:
            text += item.string
        elif item.string == None: #Must contain additional nested tags?
            for i in item.strings:
                text += i
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

def is_community_focused(description):
    '''parse description to look for specified keywords'''
    d = description
    result = False

    if 'community' in d or 'neighborhood' in d:
        if 'accessible to' in d:
            result = True
        if 'build' in d:
            result = True
        if 'benefit' in d:
            result = True
        if 'come together' in d:
            result = True
        if 'local' in d:
            result = True
    return result