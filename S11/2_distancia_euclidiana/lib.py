# NoMoreHomework

from math import sqrt

def dist_euclidiana(x, y):
    dist = []
    
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                dist.append(sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2))

    dist.sort()
    return dist[0]
