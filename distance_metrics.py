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

# Hamming Distance

def hamming(array1,array2):
    dist = 0
    for i,j in zip(array1,array2):
        if i == j:
            dist += 1
    return dist

# Minkowski Distance

def minkowski(array1,array2, p=1):
    """_summary_

    Args:
        array1 (list): list of coordinates for first point
        array2 (list): list of coordinates for second point
        p (int): equation parameter - Defaults to 1.
        {
            p = 1 (Manhattan Distance)
            p = 2 (Euclidean Distance)
            p -> infinity (Chebyshev Distance)
        }

    Returns:
        int: distance between the two vector points
    """
    sum = 0
    for i, j in zip(array1, array2):
        sum += abs((i-j)**p)
    distance = round(sum**(1/p), 2)
    return distance

# Chebyshev Distance

def chebyshev(array1, array2):
    distances = []  # Distances between each corresponding point e.g (x1,y1),(x2,y2)
    for a,b in zip(array1, array2):
        distances.append(abs(a - b))
    return max(distances)