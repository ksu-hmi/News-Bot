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
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8&as_qdr=w'.format(query) #this is the actual query we are going to scrape    
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


def googleScholarSearch(query):
    g_clean = [] #this is the list we store the search results
    url = 'https://www.scholar.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8&as_qdr=w'.format(query) #this is the actual query we are going to scrape    
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
                if(re.search('scholar.google.com', domain.netloc)):
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


def jamiaSearch(query):
    g_clean = [] #this is the list we store the search results
    url = 'https://jamianetwork.com/searchresults?q={}&allSites=1&SearchSourceType=1&exPrm_qqq=%7b!payloadDisMaxQParser+pf%3dTags+qf%3dTags%5e0.0000001+payloadFields%3dTags+bf%3d%7d%22{}%22&exPrm_hl.q={}&sort=Newest' #this is the actual query we are going to scrape    
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
                if(re.search('jamanetwork.com', domain.netloc)):
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
keyword = "Puppies"
G_url_results = googleSearch(keyword)
GS_url_results = googleScholarSearch(keyword)
J_url_results = JamiaSearch(keyword)
database = r"dbVIAA.db"
conn = create_connection(database)

#Insert into table
def create_url(conn, website_name, url,keyword):
    """
    Create a new url into the url table
    :param conn:
    :param url:
    :return: url id
    """
    sql = ''' INSERT INTO url(website_name,url,keyword)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (website_name, url, keyword))
    conn.commit()
    return cur.lastrowid

for url in G_url_results:
    #Get Domian name
    info = get_tld(url, as_object=True)
    create_url(conn, info.domain, url, keyword)    

for url in GS_url_results:
    #Get Domian name
    info = get_tld(url, as_object=True)
    create_url(conn, info.domain, url, keyword)  

for url in J_url_results:
    #Get Domian name
    info = get_tld(url, as_object=True)
    create_url(conn, info.domain, url, keyword)  