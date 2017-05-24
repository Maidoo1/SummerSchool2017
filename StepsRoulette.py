# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:14:21 2017
Летняя Школа 2017
Задача 3
@author: Мальцев Илья
"""
import math
import pylab
from matplotlib.mlab import frange

all_steps = int(input('Введите количество шагов: '))

if all_steps % 2 == 1:
    all_steps -= 1

def cathalan(n):
    cathalan = math.factorial(2*n)/(math.factorial(n) * math.factorial(n+1))
    
    return cathalan
    
def chance_of_alive(all_steps):
    
    step_forward = 1/3; step_back = 2/3
    forward_coefficient = 1; back_coefficient = 3
    chance_of_fall = 0; summ_cof = 0
    
    for step in range(0, all_steps+2, 2):
        
        if step >= 4:
            chance_of_fall = (step_forward**(step - forward_coefficient) * step_back**(step - back_coefficient)) * cathalan(step/2)
            forward_coefficient += 1
            back_coefficient += 1
        else:
            chance_of_fall = step_forward**step * cathalan(step/2)
            
        summ_cof += chance_of_fall
        
    chance_of_alive = 2 - summ_cof
    
    return chance_of_alive

print('Шансы на выживание: ', chance_of_alive(all_steps))

xlist = frange(0, all_steps, 1)
ylist = [chance_of_alive(n) for n in xlist]

pylab.plot(xlist, ylist)
pylab.show()