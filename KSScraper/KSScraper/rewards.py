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