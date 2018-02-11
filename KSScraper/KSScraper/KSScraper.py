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

print('Starting scrape of ' + str(len(pages)) + ' projects...')
print('------------------------------------------\n')

for page in pages:
    count += 1

    #Retrieve soup object
    soup = BeautifulSoup(page.content, 'html.parser')

    ####################
    # Basic Project Info
    ####################
    
    print('---------- Project # ' + str(count) + ' ----------')
    print('Project Name: ' + get_project_title(soup))
    print('Project Description Word Count: ' + str(len(str(get_project_description(soup)).split(' '))))
    print('Project Risks Word Count: ' + str(len(str(get_project_risks(soup)).split(' '))))
    #print('Project risk text: ' + str(get_project_risks(soup)))
    
    ####################
    # Rewards Data
    ####################
    
    #Retrieve objects associated with rewards
    all_rewards = get_rewards(soup)
    
    #Gather lists from retrieved rewards
    all_rewards_list = get_rewards_list(all_rewards)
    available_rewards_list = get_rewards_available_list(all_rewards)
    unavailable_rewards_list = get_rewards_unavailable_list(all_rewards)
    limited_rewards_list = get_rewards_limited_list(all_rewards)
    tiers_rewards_list = get_rewards_tiers(all_rewards_list)

    #Gather counts for final output
    rewards_count_all = get_rewards_count(all_rewards_list)
    rewards_count_available = get_rewards_count(available_rewards_list)
    rewards_count_unavailable = get_rewards_count(unavailable_rewards_list)
    rewards_count_limited = get_rewards_count(limited_rewards_list)
    rewards_count_tiers = get_rewards_count(tiers_rewards_list)

    #Output counts
    print('All rewards: ' + str(rewards_count_all))
    print('Rewards Available: ' + str(rewards_count_available))
    print('Rewards Unavailable: ' + str(rewards_count_unavailable))
    print('Rewards with Limit: ' + str(rewards_count_limited))
    print('Unique Reward Tiers: ' + str(rewards_count_tiers))

    #Updates/Counts
    updates_count = get_project_updates_count(soup)
    comments_count = get_project_comments_count(soup)
    print('Project Updates Count: ' + str(updates_count))
    print('Project Comments Count: ' + str(comments_count))

    print('\n')

print('\n------------------------------------------')
print('\nScrape Complete!')