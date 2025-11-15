# Manhattan Distance between multiple points

def calc_distance(array1, array2):
    sum = 0
    for i, j in zip(array1, array2):
        sum += abs(i-j)
    return sum

def manhattan(*args):
    distance = {} # dixtance between each point
    for i,j in enumerate(args):
        for k,m in enumerate(args):
            distance[i,k] = calc_distance(j,m)
            
    return distance