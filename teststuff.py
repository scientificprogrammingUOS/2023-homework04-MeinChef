import numpy as np

a = np.arange(10)
b = np.arange(10)[::-1]
c = np.array([10])
# Needs a sequence (in this case a tuple) of array-likes
print(np.concatenate((a,c,b)));
print(a);
print(b);
print(c);