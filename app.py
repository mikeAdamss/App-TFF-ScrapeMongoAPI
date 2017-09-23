#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

# ---- BUILD THIS NEXT .py YOURSELF ----
# These three variables are all thats in there, and all thats not on github
from NOT_FOR_GITHUB import mongoURI, getScrape, doScrape


# Mine
from mongoFunctions import updateDb

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = mongoURI

mongo = PyMongo(app)

# Just 1 response. Whole thing 
@app.route('/' + getScrape)
def serve():
    myData = [doc for doc in mongo.db.raidKills.find()]

    # Pop the id out as it wont jsonify
    for doc in myData:
        doc.pop('_id')
    
    return jsonify(myData)


# Manually Starts the database scrape-update mechanic.
@app.route('/' + doScrape)
def scrape():
    updateDb(mongo)
    return "Scrape Complete"


if __name__ == '__main__':
    
    # Update on server startup
    updateDb(mongo)
    
    # run 
    app.run(debug=True)