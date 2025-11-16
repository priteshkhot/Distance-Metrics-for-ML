# Euclidean Distance
def euclidean(array1, array2):
    sum = 0
    for i, j in zip(array1, array2):
        sum += (i-j)**2
    distance = round(sum**(1/2), 2)
    return distance

# Manhattan Distance
def manhattan(array1, array2):
    sum = 0
    for i, j in zip(array1, array2):
        sum += abs(i-j)
    return sum

# Jaccard Distance

def jaccard(array1, array2):
    intersect = len(array1 & array2)
    union = len(set(array1+array2))
    return round(intersect/union, 2)