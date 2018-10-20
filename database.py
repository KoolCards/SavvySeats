import pyrebase
import numpy as np
from random import shuffle
import random

config = {
    "apiKey": "AIzaSyDSTS0M0po8Y7szvxKD1KOCEvgeFtBFjEk",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://savvyseats-220013.firebaseio.com/",
    "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

backing = np.zeros((147, 5))
for user1 in range(0, 147):
    for pref in range(0, 5):
        backing[user1][pref] = pref + 1
    shuffle(backing[user1])

print(backing)

for user1 in range(0, 147):
    for pref in range(0, 5):
        db.child(user1).child("pref").update({pref: backing[user1][pref]})
        db.child(user1).child("states").update({pref: random.randint(0,1)})