import numpy as np
import random
from random import shuffle
import pyrebase


def initialize():
    config = {
        "apiKey": "AIzaSyDSTS0M0po8Y7szvxKD1KOCEvgeFtBFjEk",
        "authDomain": "projectId.firebaseapp.com",
        "databaseURL": "https://savvyseats-220013.firebaseio.com/",
        "storageBucket": "projectId.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database().get()
    rows = len(db.val())
    return db, rows

def retrieve_pref(db, rows, features = 5):
    #print(rows, features)
    data = np.zeros(shape = (rows, features))
    for user1 in range(0, rows):
        for pref in range(0, features):
            data[user1][pref] = db.val()[user1]["pref"][pref]
    return data

def retrieve_states(db, rows, features = 5):
    states = np.zeros(shape = (rows, features))
    for user1 in range(0, rows):
        for pref in range(0, features):
            states[user1][pref] = db.val()[user1]["states"][pref]
    return states


def initialize_preference(features = 5):
    a = np.zeros(shape = (rows, features))
    b= [i for i in range(1, features + 1)]
    for i in range(0, len(a)):
        shuffle(b)
        a[i] = np.array(b)
    return a

def compare_scores(index1, index2,mat, preferences):
    res = 42
    for i in range(1, len(preferences[index1]) + 1):
        if(mat[index1][i-1] == mat[index2][i-1]):
            res -= (preferences[index1][i-1] + preferences[index2][i-1])
    return res

def construct_mat(mat, data_pref):
    total = np.zeros(shape = (len(mat), len(mat)))
    for i in range(0, len(total)):
        for j in range(0, len(total)):
            total[i][j] = compare_scores(i, j,mat, data_pref)
    return total

def find_smallest_and_not_visited(distances, visited):
    lowest = 10000000000000000
    ix = []
    for i in range(0, len(distances)):
        if(distances[i] < lowest and not visited[i]):
            ix = [i]
            lowest = distances[i]
        elif(distances[i] == lowest and not visited[i]):
            ix.append(i)
        else:
            pass
    return lowest, random.choice(ix)

def sort_tuple(distances):
    new = enumerate(distances)
    return sorted(new, key=lambda x: x[1])

def djikstra(similarity_matrix, start_x = 0):
    visited = [False for i in range(0, len(similarity_matrix))]
    distances = [100000000 for i in range(0, len(similarity_matrix))]
    distances[start_x] = 0
    while(not all(visited)):
        distance,cell = find_smallest_and_not_visited(distances, visited)
        #print('Im currently at cell %s, with distance: %s' %(cell, distance))
        visited[cell] = True
        curr_distance = distances[cell]
        for i in range(0, len(similarity_matrix[cell])):
            if(not visited[i]):
                    distances[i] = min(curr_distance + similarity_matrix[cell][i], distances[i])
        #print(distances)
    return sort_tuple(distances)

def returnRes(result):
    newRes = np.random.rand(rows, 1)
    for currIndex in range(0, rows):
        newRes[currIndex] = result[currIndex][0]
    return newRes, total

db, rows = initialize()
data_pref = retrieve_pref(db, rows)
states = retrieve_states(db, rows)
total = construct_mat(states, data_pref)
result = djikstra(total)
newRes, total = returnRes(result)
