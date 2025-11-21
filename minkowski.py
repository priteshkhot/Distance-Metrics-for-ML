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