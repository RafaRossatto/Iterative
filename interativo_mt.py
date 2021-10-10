#aqui vamos calcular uma autoconsistencia usando o metoddo iterativo

import time
import math
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# aqui inicia o relogio

'''

Aqui temos um comentario
mag : magnetização
magold = representa magnetização antiga

'''

columns = ["Temperatura","Magnetização"]


start = time.perf_counter() 
mag = 1.5 
magold = 5.0
delta = 1.0 
temp= 1.6*10**-19
list_mag_x_temp = []
 
while (temp <= 1.10):
    delta = 1.00
    magold = 5.50
   
    while(delta >=1.0*10**-10):
        mag = math.tanh((1.0/temp) * magold)
        delta = math.fabs(mag-magold)
        magold = mag;
    
    list_mag_x_temp.append([temp,magold])
    temp += 1.0*10**-3
    
final = time.perf_counter() - start
print("time",final)
mag_x_temp = pd.DataFrame(list_mag_x_temp, columns=columns)
mag_x_temp.to_csv("mag_x_temp.csv",index=False)

#aqui bloco para plot
np_list = np.array(list_mag_x_temp)
x, y = np_list.T
plt.scatter(x, y)
plt.show()