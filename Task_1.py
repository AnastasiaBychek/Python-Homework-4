from random import random
from math import sqrt
 
d=int(input("введите точность пи"))
h=0
for i in range(1,d):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist<=1:
        h+=1
        
pi=4*(h/d)
print('Значение пи составляет% s'%pi)
