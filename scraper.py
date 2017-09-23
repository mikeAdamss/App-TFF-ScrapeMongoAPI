# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, json

from constants import SCRAPE_TIERS, TIER_NAMES


# Takes a list of tier integers, and returns dictionary per tier
def getRaidData():
    
    raidData = {}
    for tier in SCRAPE_TIERS:
        
        try:
            name = TIER_NAMES['tier' + str(tier)]
        except:
            name = 'Unknown Tier Name. Please update constants.py'
                              
        raidData.update({name:scrapeATier(tier)})
    
    return raidData
        

# creates a dictionary summarising wowproggress info for a raid tier
def scrapeATier(tier):
    
    # GET catch
    try:
        url = 'https://www.wowprogress.com/guild/eu/arathor/The+Forgotten+Few/rating.tier{t}'.format(t=tier)
        data = requests.get(url).content
    except:
        raise ValueError("Cannot scrape:", url, 'Returing status code:', data.status_code)
    
    # BS4 parsing catch
    soup = BeautifulSoup(data, 'lxml')
        
    table = soup.find_all('table', {'class':'rating'})
    
    cells = []
    rows = []
    for t in table:
        for c in t:
            if "display:none" in str(c):
                rows.append(cells)
                cells = []
            if '<td>' in str(c) and len(c.text) > 0:
                cells.append(c.text)
    return rows
