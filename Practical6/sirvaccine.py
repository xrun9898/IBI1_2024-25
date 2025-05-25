'''
def previous program as genplot
loop ten times
change the initial s and r values due to the vaccine
show the plot

'''
import numpy as np  
import matplotlib.pyplot as plt  
plt.figure(figsize=(6,4), dpi = 200)
def genplot(p) :
    s = 9999 -1000*p
    i = 1     
    r = 1000* p
    sarray = [s] 
    iarray = [i]  
    rarray = [r] 
    days = [0]  
    gamma = 0.05
    beta = 0.3 
    for day in range(1, 1000):  
        ran = np.random.rand(i)  
        for num in ran:  
            if num < gamma:  
                i -= 1  
                r += 1  
            if num < beta * (s /10000):  
                if s > 0:    
                    i += 1  
                    s -= 1  
        i = max(i, 0)  
        s = max(s, 0)  

        sarray.append(s)  
        iarray.append(i)  
        rarray.append(r)  
        days.append(day)  

    plt.plot(days, iarray, label=f'{10*p} %')  
for p in range (11):
    genplot(p)

plt.xlabel('time')  
plt.ylabel('number of people')  
plt.title('SIR Model with different vacciane rate')  
plt.legend()  
plt.grid()  
plt.show()  

