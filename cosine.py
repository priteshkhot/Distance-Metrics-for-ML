def dot_product(array1,array2):
    dot_sum = 0
    for i,j in zip(array1,array2):
        dot_sum += i*j
    return dot_sum

def cross_product(array1,array2):
    mag_array1 = 0
    mag_array2 = 0 
    for i in array1:
        mag_array1 += i**2
    for j in array2:
        mag_array2 += j**2
        
    return (mag_array1**(1/2))*(mag_array2**(1/2))

def cosine_distance(*args):
    distance = {} # dixtance between each point
    for i,j in enumerate(args):
        for k,m in enumerate(args):
            distance[i,k] = dot_product(j,m)/cross_product(j,m)
    return 