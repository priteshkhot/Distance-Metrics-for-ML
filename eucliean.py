# Euclidean Distance between multiple points
def calc_distance(array1, array2):
    sum = 0
    for i, j in zip(array1, array2):
        sum += (i-j)**2
    distance = round(sum**(1/2), 2)
    return distance

def euclidean(*args):
    distance = {} # dixtance between each point
    for i,j in enumerate(args):
        for k,m in enumerate(args):
            distance[i,k] = calc_distance(j,m)
            
    return distance
