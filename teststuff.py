import numpy as np
if __name__ == "__main__":
# use this for your own testing!
    """
    a = np.arange(9)
    print(a)
    b = a.reshape(3,3)
    print(b)
    c = np.arange(6)
    b = c.reshape(2,3)
    print(b)
    b = c.reshape(3,2)
    print(b[0][0])
    print(b[0][1])
    print("\n")
    print(b[1][0])
    print(b[1][1])
    print("\n")
    print(b[2][0])
    print(b[2][1])
    print(b)
    
    helpme = np.empty(shape = (8,6), dtype = np.bool_)
   # helpme = helpme.reshape(6,8)
    print(helpme)
 
    z = np.arange(100).reshape((10,10))
    print(z)
   # print(z[0:int(z.shape),0:8:2])
    #print(z.shape)

    y = np.arange(10)
    mask = y%2 == 0
    print(y[mask])
    """
    a = (1,2)
    b = a[0]
    print(b)
    b = a[1]
    print(b)