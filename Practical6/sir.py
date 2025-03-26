'''
initialize s,i,r,day and their array
use the loop to cycle for 1000 days
generate the possibility for i 
updata s, i, r based on gamma and beta compared to possibility
ensure s, i, r greater than 0
input s, i, r, day into array
next loop
show the polt

the method may be a bit different to the content but it works as well
'''
import numpy as np  
import matplotlib.pyplot as plt  

s = 9999    
i = 1     
r = 0     
sarray = [s] 
iarray = [i]  
rarray = [r] 
days = [0]   
gamma = 0.05
beta = 0.3
plt.figure(figsize=(6,4), dpi = 300)
for day in range(1, 1000):  
    ran = np.random.rand(i)  
    for num in ran:  
        if num < gamma:  
            i -= 1  
            r += 1  
        if num < beta* (s/10000):  
            if s > 0:    
                i += 1  
                s -= 1  
    i = max(i, 0)  
    s = max(s, 0)  

    sarray.append(s)  
    iarray.append(i)  
    rarray.append(r)  
    days.append(day)  

plt.plot(days, sarray, label='Susceptible (s)')  
plt.plot(days, iarray, label='Infected (i)')  
plt.plot(days, rarray, label='Recovered (r)')  
plt.xlabel('time')  
plt.ylabel('numbers of people')  
plt.title('SIR Model')  
plt.legend()  
plt.grid()  
plt.show()  

