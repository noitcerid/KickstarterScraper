import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

from rewards import *
from basics import *
from media import *
from data import *

#Create object to store pages to be retrieved
pages = get_pages()

count = 0

print('Starting scrape of ' + str(len(pages)) + ' pages on Kickstarter...')

for page in pages:
    count += 1

    #Retrieve soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    ####################
    # Basic Project Info
    ####################
    
    print('------------------------------------------')
    print('Project Name: ' + get_project_title(soup))
    print("Project #: " + str(count))

    ####################
    # Rewards Data
    ####################

    all_rewards = get_rewards(soup)
    all_rewards_list = get_rewards_list(all_rewards)
    available_rewards_list = get_rewards_available_list(all_rewards)
    rewards_count_all = get_rewards_count(all_rewards_list)
    rewards_count_available = get_rewards_available_count(available_rewards_list)

    print('All rewards: ' + str(rewards_count_all))
    print('Rewards Available: ' + str(rewards_count_available))


print('\nScrape Complete!')