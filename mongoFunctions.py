#!flask/bin/python
"""
Updates mongo DB using the scraper.
"""

from pymongo import MongoClient
from constants import FORCED_ORDER
from scraper import getRaidData
import json, os
from time import gmtime, strftime

TESTING = False   # switch to use local rather than scraping. For testing/playing without pissing someone off.


# For testing. In production "jsonData" comes from the scraper. Only when TESTING=False
def fakeScrape():
    
    with open("ExampleScrapeData.json", "r") as f:
        jsonData = json.load(f)
    return jsonData
    

# Dump the Json-style scrape just in case theres an issue
def backupScrape(scrape):
    
    myTime = str(strftime("%Y-%m-%d %H:%M:%S", gmtime())).replace(':', '-')
    with open(os.getcwd() + '/backups/scrapes/scrapeBU -GMT- {t}.json'.format(t=myTime), 'w') as f:
        json.dump(scrape, f)


# Returns json details for 1 raid. Contains multiple boss kills.
def scrapeAsJson(scrape):
    
    """
    Scrape shape: One boss within one list entry within one tier.
    -----------------------
    "Tomb of Sargeras": [
        [
        "+ H: Fallen Avatar",
        "4 days ago",
        "13123",
        "7048",
        "43",
        "26m 33s"
        ],
        [ 
       Another boss as above....
       ],
    ]
    """

    tierData = {}
    for tierName in scrape.keys():
        
        difficultyData = {}
        for difficulty in ['+ M', '+ H', '+ N']:
        
            bossData = {}
            for bossKillData in scrape[tierName]:
                
                bossName = bossKillData[0]

                # Only continue if its the difficulty we're currently parsing for
                if difficulty in bossName:
                    
                    # We can get rid of the difficulty tag now
                    bossName = bossName.replace(difficulty, '').replace(':', '').strip()
                    
                    # fastest kill catch (is sometimes blank)
                    try:
                        fKill = bossKillData[5]
                    except:
                        fKill = ''
                        
                    # Going to force a nice order, but keeping it optional so I dont "have to" as soon as new content is out
                    try:
                       order = FORCED_ORDER[bossName] 
                    except:
                       order = 'New' 
                     
                    bossStats = {
                                 'First Kill':bossKillData[1],
                                 'World':bossKillData[2],
                                 'EU':bossKillData[3],
                                 'Realm':bossKillData[4],
                                 'Fastest Kill':fKill,
                                 'Order':order
                                }
                        
                    bossData.update({bossName:bossStats})
            difficultyData.update({difficulty:bossData})
        tierData.update({tierName:difficultyData})
    
    return tierData
    
    
                    

# takes the data from the webscrape and updates our Mongo db with
# the next wescrape. Shift our sequence (backups) back 1 place and deleting the oldest
def updateDb(mongo):
    
    """
    
    This is the shape of the collection
    -----------------------------------
    
     'description': 'Raid Progress Scrapes from WowProgress',
     'last_update_successful': 'N',
     'last_updated': '',
     'sequence': <<scrapeAsJson>>
     'title': 'TFF Raid Progress'}
 
    """
    
    # Ready Mongo
    db = mongo.db
    
    # Load Scraped Data
    if TESTING:
        scrape = fakeScrape()
    else:
        scrape = getRaidData()

    
    # Get scrape inot json shapd for db
    tierData = scrapeAsJson(scrape)   # as-a-list as thats how it is in db
    
    #Write to db
    db.raidKills.update({"title":"TFF Raid Progress"}, {'$set':{"sequence":tierData}})
    
    # Timestamo
    db.raidKills.update({"title":"TFF Raid Progress"}, {'$set':{"last_updated":strftime("%Y-%m-%d %H:%M:%S", gmtime())}})
    strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    # Backup the json just in case
    backupScrape(tierData)


# Run everything when this script is called
if __name__ == '__main__':
    updateDb()

