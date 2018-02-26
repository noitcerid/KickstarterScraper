import requests
#from pip._vendor import requests
from bs4 import BeautifulSoup

def get_image_list(soup):
    '''Returns list of images found -> list'''
    images = []
    #get all images
    all_image_tags = list(soup.body.find_all('img'))
    #exclude videos, social media, and avatars
    for tag in all_image_tags:
        avatar_class = 'avatar inline-block align-middle circle w6 h6 ml2 bg-grey-100'
        avatar_class2 = 'avatar-small circle'
        about_creator = 'circle bg-grey-500 w4 h4 w7-md h7-md flex-noshrink mb2-md'
        video_class = 'has_played_hide full-width poster landscape'
        facebook = 'https://www.facebook.com/'
        tag_s = str(tag)
        if video_class not in tag_s and avatar_class not in tag_s and about_creator not in tag_s and avatar_class2 not in tag_s and facebook not in tag_s:
            images.append(tag)
            #print('\n' + str(tag))
    return images

def get_image_count(image_list):
    '''Counts number of items in list -> int'''
    return len(image_list)

def get_video_list(soup):
    '''Returns list of videos found -> list'''
    videos = list(soup.body.find_all('video', class_='landscape'))
    return videos

def get_video_count(video_list):
    '''Counts number of items in list -> int'''
    return len(video_list)