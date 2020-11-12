#NewsFeed that houses search results
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
from VIAA_Database import *
from tld import get_tld
import sqlite3
from sqlite3 import Error
 
def googleSearch(query):
    g_clean = [] #this is the list we store the search results
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query) #this is the actual query we are going to scrape    
    try:
        html = requests.get(url)
        if html.status_code==200:
            soup = BeautifulSoup(html.text, 'lxml')
            a = soup.find_all('a') # a is a list
        for i in a:
            k = i.get('href')
            try:
                m = re.search("(?P<url>https?://[^\s]+)", k)
                n = m.group(0)
                rul = n.split('&')[0]
                domain = urlparse(rul)
                if(re.search('google.com', domain.netloc)):
                    continue
                else:
                    g_clean.append(rul)
                        
            except:
                continue
    #prints the errors            
    except Exception as ex:
        print(str(ex))
    finally:
        return g_clean

#just for testing
query = "Puppies"
url_results = googleSearch(query)

database = r"db\VIAA..db"
conn = create_connection(database)

#Insert into table
def create_url(conn, website_name, url):
    """
    Create a new url into the url table
    :param conn:
    :param url:
    :return: url id
    """
    sql = ''' INSERT INTO url(website_name,url)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (website_name, url))
    conn.commit()
    return cur.lastrowid

for url in url_results:
    #Get Domian name
    info = get_tld(url, as_object=True)
    create_url(conn, info.domain, url)    