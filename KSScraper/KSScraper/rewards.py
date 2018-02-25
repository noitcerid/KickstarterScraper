import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

def get_rewards(soup):
    '''Returns rewards body -> BeautifulSoup.body'''
    body = soup.body
    rewards = body.find('div', class_='NS_projects__rewards_list')
    return rewards

def get_rewards_list(rewards_body):
    '''Returns all rewards -> list object'''
    rewards_list = list(rewards_body.find_all('span', class_='money'))
    return rewards_list

def get_rewards_available_list(rewards_body):
    '''Returns rewards available -> list object'''
    rewards_available_list = list(rewards_body.find_all('li', class_='hover-group js-reward-available pledge--available pledge-selectable-sidebar'))
    return rewards_available_list

def get_rewards_unavailable_list(rewards_body):
    '''Returns rewards available -> list object'''
    rewards_unavailable_list = list(rewards_body.find_all('li', class_='hover-group pledge--all-gone pledge-selectable-sidebar'))
    return rewards_unavailable_list

def get_rewards_count(rewards):
    '''Returns how many rewards were found -> int'''
    return len(rewards)

def get_rewards_tiers(rewards):
    '''Returns a unique list of rewards for determining "tiers" -> list'''
    output = []
    for x in rewards:
        if x not in output:
            output.append(x)
    return output

def get_rewards_limited_list(rewards_body):
    '''Returns a list of records considered to have limited numbers of backers available -> list'''
    limited = []
    #gather limited gone only
    limited_gone = list(rewards_body.find_all('span', class_='pledge__limit pledge__limit--all-gone mr2'))
    
    #gather all (filtering in for loop to only those that contain "Limited" text
    limited_available = list(rewards_body.find_all('span', class_='pledge__limit'))

    #we know we can add the entries that are gone since they're filtered properly already
    limited = limited_gone

    #conditionally check for text and add if present
    for p in limited_available:
        if p.string == 'Limited':
            limited.append(p)
    return limited