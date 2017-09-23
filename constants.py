# -*- coding: utf-8 -*-

"""
The tiers we are actually going to scrape
"""
SCRAPE_TIERS = [19, 20]



"""
Wont know the tier names until they're announced. When we do they go in here.
"""
TIER_NAMES = {
              'tier20':'Tomb of Sargeras',
              'tier19':'Emerald Nightmare, Trial of Valour & Nighhold'
              }

"""
The following is an arbitrary count to order bosses. We'll start it at 500 (space for old content...just in case),
the FORCED_ORDER of each boss will be written to the dicts then into mongoDb. Database can order as needed.
"""

FORCED_ORDER = {
        "Nythendra":500,
        "Ursoc":501,
        "Dragons of Nightmare":502,
        "Elerethe Renferal":503,
        "Il'gynoth":504,
        "Cenarius":505,
        "Xavius":506,
        "Odyn":507,
        "Guarm":508,
        "Helya":509,
        "Skorpyron":510,
        "Chronomatic Anomaly":511,
        "Trilliax":512,
        "Spellblade Aluriel":513,
        "Krosus":514,
        "Tichondrius":515,
        "Star Augur Etraeus":516,
        "High Botanist Tel'arn":517,
        "Grand Magistrix Elisande":518,
        "Gul'dan":519,
        "Goroth":520,
        "Demonic Inquisition":521,
        "Harjatan":522,
        "Mistress Sassz'ine":523,
        "Sisters of the Moon":524,
        "The Desolate Host":525,
        "Maiden of Vigilance":526,
        "Fallen Avatar":527,
        "Kil'jaeden":528
        }
