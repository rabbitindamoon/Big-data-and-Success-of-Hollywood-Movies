import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from random import choice
import random

def link_cleaner(soup_link):
    soup_string = str(soup_link)
    soup_clean = re.sub("<.*?>", "", soup_string)
    return soup_clean
counter_to_stop = 0
def fetch_data(url,header, ttcode):
    try:
        req = Request(url, headers=header)
        page_raw = urlopen(req).read()
        return page_raw
    except:
        print("Failed trying again") 
        return ttcode; 
    

#Start by capturing images of the stones in the training_data.
#source = '/home/thorsteinngj/Documents/Skoli/Thesis/'
#train_data = pd.read_csv(source+'copenhagen_export_graves.csv')
#ids = train_data["graveid"].round(0)


webpage = "https://www.imdb.com/title/"


desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents)}
movie_failed_to_scraped = []
movie_country_missing = []
#movie_scraping_country_index = movie_scraping_country_index.assign(movie_nocountry_index = indexes_nocountry, 
#                                                                   movie_nocountry_id = movie_scraping_country_filename)
count=0
for i in range(len(movie_scraping_country_filename)):
    count+=1

    if count%10 == 0 :
        print(count)
    url_using = webpage + movie_scraping_country_filename[i]
    ua = random_headers()
    try:
        page_raw = fetch_data(url_using,ua, movie_scraping_country_filename[i])
     	#HTML parsing
        page_soup = soup(page_raw, "lxml")  # of webpagehtml
        picture = page_soup.findAll("meta",{"property":"og:image"})
        name = page_soup.head.titleDetails 
        title_details = page_soup.find(id="titleDetails")
        title_details = title_details.get_text()
        title_details = str(title_details)
        title_details= title_details.replace("\n", "")
        regex = r"(?<=Country:)(.*)(?=Language)"
        regex2 = r"(?<=Country:)(.*)(?=Filming)"
        matches = re.search(regex, title_details, re.IGNORECASE)
        try:  
            #matches = matches[0].replace(r'\n', "") 
            matches = re.search(regex, title_details, re.IGNORECASE)
            matches = matches[0]
        except:
            matches = str('None')
            #matches = re.search(regex2, title_details, re.IGNORECASE)
    except:
        matches = str('None')
        movie_failed_to_scraped.append(page_raw)
# =============================================================================
#     try:
#         matches = matches[0]
#     except:
#         matches = str('None')
#     
# =============================================================================
    movie_country_missing.append(matches)



