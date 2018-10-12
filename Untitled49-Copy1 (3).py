
# coding: utf-8

# In[2]:


import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def player_database(path,playername,team):
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter =',')
    
        runs = []
        balls = []
    
        for row in readCSV:
        
            runs.append(row[1])
            balls.append(row[2])
    while '-' in runs:
        runs.remove('-')
    while '-' in balls:
        balls.remove('-')    
    runs = list(map(int, runs))
    balls = list(map(int, balls))
    average = (sum(balls))/len(balls)
    average = round(average)
    print("Average balls is")
    print(average)
    plt.scatter(balls,runs)
    plt.show()

    def slope_intercept(x_val,y_val):
        x = np.array(x_val)
        y = np.array(y_val)
        m = (((np.mean(x)*np.mean(y)) - np.mean(x*y))/
            ((np.mean(x)*np.mean(x)) - np.mean(x*x)))
        m = round(m,2)
        b = (np.mean(y) - np.mean(x)*m)
        b = round(b,2)
        score = m*average + b
        score = round(score)
        print(score)

        return score
#slope_intercept(balls,runs)
#Score by Player 

    import requests

    url = 'https://www.jsonstore.io/a8b2f59f6c804d41b4d9abfa6f8263847b401cdd06bc63950642bd1302ecc788'+ team + str(playername)
    data = {"balls": average,
            "score": slope_intercept(balls,runs)
           }
    r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
    return 0
india = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for x in india:
    player_database('C:\\Users\\Ayush\\Desktop\\India\\'+ str(india[x]) +'.csv',str(india[x]), 'India123')
    

