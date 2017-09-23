# App-TFF-ScrapeMongoAPI

A learning exercise with a real-world use. Scrapes gaming data from wowprogress. Restructures and reads into a mongo database. App has an API where the scraper can be triggered or the data requested.

Deploys via heroku.


# MongoDb

Needs something like the below (a callection, "raidKills"), otherwise the only fields directly referenced in-script are "last_updated" and "sequence".

```json
{
"description": "Raid Progress Scrapes from WowProgress",
"last_update_successful": "YY",
"last_updated": "2017-09-23 09:39:36",
"sequence": {
"Emerald Nightmare, Trial of Valour & Nighhold": {},
"Tomb of Sargeras": {}
},
"title": "TFF Raid Progress"
}

```

# Re-Use

I personally wouldn't reuse someones learning exercise :), but if you want to you'll need to change the url strings in scraper.py to point at a differente wowguild. You'll also need to add three variables in a file called NOT_FOR_GITHUB.py (see notes in app.py).
