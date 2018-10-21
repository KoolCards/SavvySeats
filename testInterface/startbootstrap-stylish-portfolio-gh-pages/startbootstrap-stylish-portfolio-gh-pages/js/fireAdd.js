var config = {
    apiKey: "AIzaSyDSTS0M0po8Y7szvxKD1KOCEvgeFtBFjEk",
    authDomain: "savvyseats-220013.firebaseapp.com",
    databaseURL: "https://savvyseats-220013.firebaseio.com/",
    projectId: "savvyseats-220013",
    storageBucket: "<BUCKET>.appspot.com",
    messagingSenderId: "<SENDER_ID>"
};

var defaultApp = firebase.initializeApp(config);
var defaultDatabase = defaultApp.database();
