from matplotlib import pyplot as plt
import numpy as np
import random
from random import shuffle

rows = 550
features = 6
mat = np.random.rand(rows, features)
mat[mat > 0.5] = 1.0
mat[mat <= 0.5] = 0.0

def initialize_preference():
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

def construct_mat(mat):
    total = np.zeros(shape = (len(mat), len(mat)))
    preferences = initialize_preference()
    for i in range(0, len(total)):
        for j in range(0, len(total)):
            total[i][j] = compare_scores(i, j,mat, preferences)
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
        print('Im currently at cell %s, with distance: %s' %(cell, distance))
        visited[cell] = True
        curr_distance = distances[cell]
        for i in range(0, len(similarity_matrix[cell])):
            if(not visited[i]):
                    distances[i] = min(curr_distance + similarity_matrix[cell][i], distances[i])
        print(distances)
    return sort_tuple(distances)

np.set_printoptions(threshold=np.inf)
total = construct_mat(mat)
print(total)
print('*********************8')
result = djikstra(total)
print(result)
