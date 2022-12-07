""" Вычислить число Пи c заданной точностью d
Пример:
 - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10 """

import math

d= str(input('Enter number d - '))
print(math.pi)
len_d = len(d.split('.')[1])

i=0
num_pi= str(math.pi)
while i < (len_d+2) and i < len(num_pi):
    print(num_pi[i], end ="")
    i+=1

