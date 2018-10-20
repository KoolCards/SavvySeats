import pyrebase

config = {
    "apiKey": "AIzaSyDSTS0M0po8Y7szvxKD1KOCEvgeFtBFjEk",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://savvyseats-220013.firebaseio.com/",
    "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.child("users").push("data")

