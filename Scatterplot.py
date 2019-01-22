# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:49:16 2018

@author: Kau
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatch




def S_Plot(x, y, a, b):
    #define scatter plot values, plot them.
    plt.scatter(x[0:50], y[0:50], color = "red")
    plt.scatter(x[50:100], y[50:100], color = "blue")
    plt.scatter(x[100:150], y[100:150], color = "green")
    #define legend values
    red_patch = mplpatch.Patch(color='red', label = 'Iris_Setosa')
    blue_patch = mplpatch.Patch(color='blue', label = 'Iris_Versicolor')
    green_patch = mplpatch.Patch(color='green', label = 'Iris_Virginica')
    #set title, output legend, labels.
    plt.title(a + ' vs ' + b)
    plt.legend(handles = [red_patch, blue_patch, green_patch], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.savefig('scatter'+a+b, bbox_inches = 'tight', dpi = 100)
    plt.show()

def main():
    a = np.loadtxt('iris.data', usecols = (0, 1, 2, 3), delimiter = ',')
    #define values for sepal columns.
    Sepal_L = a[0:150, 0]
    Sepal_W = a[0:150, 1]
    Petal_L = a[0:150, 2]
    Petal_W = a[0:150, 3]
    plt.style.use("classic")
    
    #run S_PLOT 6x for all configurations.
    S_Plot(Sepal_L, Sepal_L, 'Sepal_L', 'Sepal_L')
    S_Plot(Sepal_L, Sepal_W, 'Sepal_L', 'Sepal_W')
    S_Plot(Sepal_L, Petal_L, 'Sepal_L', 'Petal_L')
    S_Plot(Sepal_L, Petal_W, 'Sepal_L', 'Petal_W')
    S_Plot(Sepal_W, Sepal_L, 'Sepal_W', 'Sepal_L')
    S_Plot(Sepal_W, Sepal_W, 'Sepal_W', 'Sepal_W')
    S_Plot(Sepal_W, Petal_L, 'Sepal_W', 'Petal_L')
    S_Plot(Sepal_W, Petal_W, 'Sepal_W', 'Petal_W')
    S_Plot(Petal_L, Sepal_L, 'Petal_L', 'Sepal_L')
    S_Plot(Petal_L, Sepal_W, 'Petal_L', 'Sepal_W')
    S_Plot(Petal_L, Petal_L, 'Petal_L', 'Petal_L')
    S_Plot(Petal_L, Petal_W, 'Petal_L', 'Petal_W')
    S_Plot(Petal_W, Sepal_L, 'Petal_W', 'Sepal_L')
    S_Plot(Petal_W, Sepal_W, 'Petal_W', 'Sepal_W')
    S_Plot(Petal_W, Petal_L, 'Petal_W', 'Petal_L')
    S_Plot(Petal_W, Petal_W, 'Petal_W', 'Petal_W')
    
main()

