import numpy as np

z = np.random.randint(0,101,size=99)
print(z)

def FindPercentileK(ar:list,k:int):
    from math import floor
    n = len(ar)
    ar.sort()
    perc=k*n/100
    print(perc)
    if (perc)%1 == 0:
        perc=int(perc)
        return (ar[perc]+ar[perc+1])/2
    return ar[floor(perc)]

print(FindPercentileK(z[:],25))
