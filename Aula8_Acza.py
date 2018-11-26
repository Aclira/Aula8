
# coding: utf-8

# In[2]:


from IPython.display import Image
from IPython.display import HTML
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import math


# # Resolução de um sistemas triangular superior.

# In[5]:


M = np.array([[1,2,3,4], [0,5,6,7], [0,0,8,9],[0,0,0,10]])
b = np.array([5,4,4,2])

print("Matriz exemplo")
print(M)

def teste(a,b):
    n = len(a)
    x = n*[0]
    x[n-1] = b[n-1]/a[n-1][n-1]
    for k in range(n-1,-1,-1):
        s = 0
        for j in range(k+1,n):
            s = s + a[k][j]*x[j]
        x[k] = (b[k]-s)/a[k][k]                 
    return x



teste(M,b)


# In[549]:


x = np.linalg.solve(M,b)
print(x)


# # Eliminação de Gauss

# In[28]:


M = np.array([[1,-1,2],[2,1,-1],[-2,-5,3]])
b = np.array([[2],[1],[3]])

print("matriz exemplo")
print(M)

def eliminacao(a,b):
    n = len(a)
    m = n*[0]
    
    for k in range(0,n-1):
        for i in range(k+1,n):
            m=a[i][k]/a[k][k]
            a[i][k] = 0
            for j in range(k+1,n):
                a[i][j] = a[i][j] - m*a[k][j]
                b[i] = b[i] - m*b[k]
    return a
                


eliminacao(M,b)
print(b)

