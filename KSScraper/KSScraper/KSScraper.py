import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

from rewards import *
from basics import *
from media import *
from data import *
from backers import *

#Create object to store pages to be retrieved
print('Retrieving pages... please be patient!')
pages = get_pages(10)

#Create list to export to csv
scrape_results = []
#scrape_results.append(['url', 'description_word_count', 'risks_word_count', 'image_count', 'video_count', 'community_focused', 'updates_count', 'comments_count', 'rewards_count_tiers', 'rewards_count_all', 'rewards_count_limited', 'top_backer_city', 'top_backer_city_backers_count'])

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
    
    project_title = get_project_title(soup)
    project_description = str(get_project_description(soup))
    project_description_word_count = str(len(project_description.split(' ')))
    project_risks_word_count = str(len(str(get_project_risks(soup)).split(' ')))
    project_community_focused = str(is_community_focused(get_project_description(soup)))
    print('---------- Project # ' + str(count) + ' ----------')
    print('Project Name: ' + project_title)
    print('Project Description Word Count: ' + project_description_word_count)
    print('Project Risks Word Count: ' + project_risks_word_count)
    print('Community Focused?: ' + project_community_focused)
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

    #Output rewards counts
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

    #Media Counts
    images = get_image_list(soup)
    image_count = get_image_count(images)
    videos = get_video_list(soup)
    video_count = get_video_count(videos)
    print('Project Images: ' + str(image_count))
    print('Project Videos: ' + str(video_count))

    #Backer Info
    top_backer_city = str(get_top_backer_city(get_backer_cities(page)))
    top_backer_city_backers_count = str(get_top_backer_city_backers_count(get_backer_cities(page)))
    #print('Project Backer Cities: ' + str(get_backer_cities(page)))
    print('Project Top Backer City: ' + top_backer_city)
    print('Project Top City Backers Count: ' + str(top_backer_city_backers_count))

    #gather results into row and append to output
    scrape_results.append([str(page.url), project_description_word_count, project_risks_word_count, image_count, video_count, project_community_focused, updates_count, comments_count, rewards_count_tiers, rewards_count_all, rewards_count_limited, top_backer_city, top_backer_city_backers_count])

print('\n------------------------------------------')
print('\nScrape Complete!')

#Export to csv
print('\nExporting results to CSV')
with open('output.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in scrape_results:
        writer.writerow(row)