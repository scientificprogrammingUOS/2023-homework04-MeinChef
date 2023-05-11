import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array0, array1, axis = 0):
    try:
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
    pass
