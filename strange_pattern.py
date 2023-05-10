import numpy as np

# implement the function strange pattern

def strange_pattern(a): #n zeile, m spalte
    n = a[0]
    m = a[1]
    pattern = np.zeros( shape=((n,m)) , dtype = bool)
    for i in range(n):
        if(i%3 == 0):   pattern[i,0:m:3] = True;
        elif(i%3 == 1): pattern[i,2:m:3] = True;
        elif(i%3 == 2): pattern[i,1:m:3] = True;



    return pattern


if __name__ == "__main__":
    # use this for your own testing!
    #print(strange_pattern(10,10))
    pass
    
