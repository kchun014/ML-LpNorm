import numpy as np
import matplotlib.pyplot as plt

def covariance(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
#    x_m = np.full((1, len(x)), mean_x)
#    y_m = np.full((1, len(y)), mean_y)
    total = 0
    new_x = []
    new_y = []
    for i in range(len(x)):
        new_x.append(x[i] - mean_x)
        new_y.append(y[i] - mean_y)
    for i in range(len(y)):
        total += new_x[i] * new_y[i]
    return total / len(x)

def std_dev(x):
    calc_mean = np.mean(x)
    total = 0
    for i in x:
        total += np.square(i - calc_mean)
    total = total / len(x)
#    print(np.sqrt(total))
    return np.sqrt(total)

def correlation(x, y):
    sdev_x = std_dev(x)
    sdev_y = std_dev(y)
    cov_xy = covariance(x, y)
#    print(covariance(x, y))
    return cov_xy/(sdev_x * sdev_y)
    
def main():
    a = np.loadtxt('iris.data', usecols = (0, 1, 2, 3), delimiter = ',')
    b = np.loadtxt('wine.data', usecols = (0, 1, 2, 3), delimiter = ',')
    #predefine iris and wine columns.
    Sepal_L = a[0:150, 0]
    Sepal_W = a[0:150, 1]
    Petal_L = a[0:150, 2]
    Petal_W = a[0:150, 3]
    Iris_List = ['', 'Sepal_L', 'Sepal_W', 'Petal_L', 'Petal_W']
    Wine_List = ['', 'Alcohol', 'Malus_A', 'Ash']
    Alc = b[0:178, 1]
    Mal = b[0:178, 2]
    Ash = b[0:178, 3]
    plt.style.use("classic")
    Iris_data = [Sepal_L, Sepal_W, Petal_L, Petal_W]
    Wine_data = [Alc, Mal, Ash]
    #predefine arrays for wine and iris heatmap.
    Wine_Array = np.zeros(shape = (3, 3))
    Iris_Array = np.zeros(shape = (4, 4))
    #populate array and output in heatmap
    for i in range(len(Iris_data)):
        for j in range(len(Iris_data)):
            Iris_Array[i, j] = correlation(Iris_data[i], Iris_data[j])
    plt.matshow(Iris_Array)
    plt.colorbar()
    axes = plt.gca()
    axes.set_xticklabels(Iris_List)
    axes.set_yticklabels(Iris_List)
    plt.title('Iris_Heatmap')
    plt.savefig('Iris_Heatmap', bbox_inches = 'tight', dpi = 100)
    plt.show()
    
    #repeat population for wine and output.
    for i in range(len(Wine_data)):
        for j in range(len(Wine_data)):
            Wine_Array[i, j] = correlation(Wine_data[i], Wine_data[j])
    plt.matshow(Wine_Array)
    plt.colorbar()
    axes = plt.gca()
    axes.set_xticklabels(Wine_List)
    axes.set_yticklabels(Wine_List)
    plt.title('Wine_Heatmap')
    plt.savefig('Wine_Heatmap', bbox_inches = 'tight', dpi = 100)
    plt.show()
    

main()
