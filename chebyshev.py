def calc_dist(array1, array2):
    distances = []  # Distances between each corresponding point e.g (x1,y1),(x2,y2)
    for a,b in zip(array1, array2):
        distances.append(abs(a - b))
    return max(distances)

def chebyshev(*args):
    distance = {} # dixtance between each point
    for i,j in enumerate(args):
        for k,m in enumerate(args):
            distance[i,k] = calc_dist(j,m)
            
    return distance