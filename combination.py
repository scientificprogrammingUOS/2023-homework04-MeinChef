import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array0, array1, axis = 0):
    # delete the NotImplementedError when you write your function.
    try:
        #np.dtype(array0);
        #np.dtype(array1);
        array0 = np.squeeze(array0);
        array1 = np.squeeze(array1);
        print(array0);
        print(array1);

        a = np.concatenate((array0, array1));
        print(a);
        return a;
        
    except TypeError:
        print("TypeError: You didn't give a fucking array as input. Change that NOW!")



if __name__ == "__main__":
    #a = np.arange(0,4);
    #b = np.arange(5,7);
    #print(a);
    #print(b);
    #combination(a, b);
    pass
