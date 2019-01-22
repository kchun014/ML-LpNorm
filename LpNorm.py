# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:15:16 2018

@author: Kau
"""


import numpy as np
import matplotlib.pyplot as plt

iris = np.loadtxt('iris.data', usecols = (0, 1, 2, 3), delimiter = ',')
wine = np.loadtxt('wine.data', usecols = (0, 1, 2, 3), delimiter = ',')

def Manhattan(x, y):
    total = 0
    for i in range(len(x)):
        total += np.abs(x[i] - y[i])
    return total

def Euclidian(x, y):
    total = 0
    for i in range(len(x)):
        total += np.square(np.abs(x[i] - y[i]))
    total = np.sqrt(total)
    return total

def distance(x, y, p):
    result = 0
    if p == 1:
        result = Manhattan(x, y)
    elif p == 2:
        result = Euclidian(x, y)
    return result

def main():
    #populate iris arrays
    Iris_Rows = []
    Iris_Data_p1 = np.zeros(shape = (150, 150))
    Iris_Data_p2 = np.zeros(shape = (150, 150))
    
    for i in range(len(iris)):#Append rows appropriately
        Iris_Rows.append(iris[i, 0:4])

    #get distance for p1 of iris
    for i in range(len(iris)):
        for j in range(len(iris)):
            Iris_Data_p1[i, j] = distance(Iris_Rows[i], Iris_Rows[j], 1)
    np.savetxt('Iris_Data_p1.data', Iris_Data_p1)
    plt.matshow(Iris_Data_p1)
    plt.colorbar()
    #output heatmap
    plt.title('Iris_Dist_Heatmap_p1')
    plt.savefig('Iris_Dist_Heatmap_p1', bbox_inches = 'tight', dpi = 100)
    plt.show()
    
    #get distance for p2 of iris
    for i in range(len(iris)):
        for j in range(len(iris)):
            Iris_Data_p2[i, j] = distance(Iris_Rows[i], Iris_Rows[j], 1)
    np.savetxt('Iris_Data_p2.data', Iris_Data_p2)
    plt.matshow(Iris_Data_p2)
    plt.colorbar()
    #output heatmap
    plt.title('Iris_Dist_Heatmap_p2')
    plt.savefig('Iris_Dist_Heatmap_p2', bbox_inches = 'tight', dpi = 100)
    plt.show()
    
#    count = 0
#    dist = 5000
#    for j in range(len(iris)):
#            if j != 1:
#                if Iris_Data_p1[1][j] < dist:
#                    index = j
#                    dist = Iris_Data_p1[1][j]
#                    
#    print(dist, index)
    count = 0 #reset count, use for future
    for i in range(len(iris)):
        dist = 100 #set silly large distance
        index = i
        for j in range(len(iris)):
            if i != j:
                if Iris_Data_p2[i][j] < dist: #if new distance is less, update distance and index
                    index = j
                    dist = Iris_Data_p2[i][j] 
        if i < 50: #check index to see if within same class.
            if index < 50:
                count += 1
        elif i < 100:
            if (50 <= index < 100):
                count += 1
        elif i < 150:
            if index >= 100:
                count += 1
    print('Count:' + str(count))   
    
    #initialize values for array size and populate wine row
    Wine_Rows = []
    Wine_Data_p1 = np.zeros(shape = (178, 178))
    Wine_Data_p2 = np.zeros(shape = (178, 178))
    #Get distances for p1 wine
    for i in range(len(wine)):
        Wine_Rows.append(wine[i, 1:4])
    for i in range(len(wine)):
        for j in range(len(wine)):
            Wine_Data_p1[i, j] = distance(Wine_Rows[i], Wine_Rows[j], 1)
    np.savetxt('Wine_Data_p1.data', Wine_Data_p1)
    plt.matshow(Wine_Data_p1)
    plt.colorbar()
    #output heatmap
    plt.title('Wine_Dist_Heatmap_p1')
    plt.savefig('Wine_Dist_Heatmap_p1', bbox_inches = 'tight', dpi = 100)
    plt.show()
    #get distances for p1 wine
    for i in range(len(wine)):
        for j in range(len(wine)):
            Wine_Data_p2[i, j] = distance(Wine_Rows[i], Wine_Rows[j], 2)
    np.savetxt('Wine_Data_p2.data', Wine_Data_p2)
    plt.matshow(Wine_Data_p2)
    plt.colorbar()
    #output heatmap
    plt.title('Wine_Dist_Heatmap_p2')
    plt.savefig('Wine_Dist_Heatmap_p2', bbox_inches = 'tight', dpi = 100)
    plt.show()
    
    count = 0 #reset count
    for i in range(len(wine)):
        dist = 100 #reset distance to sufficiently large number
        index = i
        for j in range(len(wine)):
            if i != j:
                if Wine_Data_p1[i][j] < dist:
                    index = j
                    dist = Wine_Data_p1[i][j]
        if i < 59:#check index to count.
            if index < 59:
                count += 1
        elif i < 130:
            if (59 <= index < 130):
                count += 1
        elif i < 178:
            if index >= 130:
                count += 1
    print('Count:' + str(count))   
    
    
main()