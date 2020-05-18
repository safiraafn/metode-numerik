import numpy as np 
import math

n = int(input('Input jumlah pasangan nilai:'))
x = np.zeros((n))
y = np.zeros((n))

for k in range(0,n):
    print('Input x[{}]='.format(k), end="")
    x[k] = float(input())
    print('Input y[{}] = '.format(k), end="")
    y[k] = float(input())

h=x[1]-x[0]
Integrasi=y[0]+y[n-1]
jumlah=0
for i in range(1,n-1):
    if (i%3==0):
        jumlah=jumlah + 2*y[i]
    else:
        jumlah + 3*y[i]
Integrasi=math.pi*(3*h/8)*(Integrasi+jumlah)

print('Hasilnya=', Integrasi)