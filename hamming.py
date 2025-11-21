x1 = 10101010
x2 = 11001100

# Zip method 
def hamming(x1,x2):
    dist = 0
    for i,j in zip(str(x1),str(x2)):
        if i == j:
            dist += 1
    return dist        
    
if __name__ == "__main__":
    print(hamming(x1,x2))