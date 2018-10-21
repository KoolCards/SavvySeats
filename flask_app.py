from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
from io import BytesIO
import requests
from Djikstra import *
import json

config = {
    "apiKey": "AIzaSyDSTS0M0po8Y7szvxKD1KOCEvgeFtBFjEk",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://savvyseats-220013.firebaseio.com/",
    "storageBucket": "projectId.appspot.com"
}

features = 5

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    print('We Were just toggled')
    return 'Hello from Sachin Flask!'

@app.route('/baby')
def hello():
    print('We Were just toggled')
    return 'Hello from Sachin Flask!'


@app.route('/getOrder', methods = ['POST'])
def base():
    data = request.get_json()
    db, rows = initialize()
    data_pref = retrieve_pref(db, rows)
    states = retrieve_states(db, rows)
    total = construct_mat(states, data_pref)
    result = djikstra(total)
    newRes, total = returnRes(result, total)
    print('Accessed')
    return json.dumps({"newRes": newRes, "total": total})

if __name__ == '__main__':
  app.run(port='8080', host="0.0.0.0")
