import numpy as np
import numpy.linalg as la

def func2(i, j):
    fi = []
    for s in range(1,j+1):
        for t in range(1,i+1):
            if s==1 and t==1:
                fi.append(1)
            elif s==t:
                fi.append(0)
            elif s<t:
                fi.append(t)
            else:
                fi.append(-t)
    a=np.array(fi)
    c = a.reshape((9,9))
    return la.det(c)
            
        
        
    
print(func2 (9,9))
