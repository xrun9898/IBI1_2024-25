'''
Initialize parameters: beta, gamma, days, population_size  
Create a zero array population  
Randomly select an initial infected individual and set it to 1  

Define the color map cmap  

Initialize the plotting window  

Loop for days:  
    Find coordinates of infected individuals  
    
    For each infected individual (x, y):  
        For each neighbor (nx, ny):  
            If the neighbor is within bounds and is susceptible:  
                If random probability < beta, set neighbor to infected  
        
        If random probability < gamma, set infected individual to recovered  

    Every 5 days, plot the heatmap showing the current day  

Display the final graph  

this version's figure can show the change of infection more clearly 
'''
import numpy as np  
import matplotlib.pyplot as plt  
from matplotlib.colors import ListedColormap  

beta = 0.3   
gamma = 0.05   
days = 100
population_size = (100, 100)
population = np.zeros(population_size)   
outbreak = np.random.choice(range(100), 2)  
population[outbreak[0], outbreak[1]] = 1 
colors = ['blue', 'green', 'yellow']  
cmap = ListedColormap(colors)  
plt.figure(figsize=(16, 10), dpi=100)  
for time in range(days):  
    infected_indices = np.argwhere(population == 1)  
    for i in infected_indices:  
        x, y = i[0], i[1]      
        for dx in [-1, 0, 1]:  
            for dy in [-1, 0, 1]:  
                if dx == 0 and dy == 0:  
                    continue  
                nx, ny = x + dx, y + dy  
                if 0 <= nx < (population_size)[0] and 0 <= ny < (population_size)[1]:    
                    if population[nx, ny] == 0 and np.random.rand() < beta:  
                        population[nx, ny] = 1  
        if np.random.rand() < gamma:  
                population[x, y] = 2   
    if time % 5 == 0:      
        plt.imshow(population, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)  
        plt.title(f'days: {time}')  
        plt.axis('off')  
        plt.pause(0.1) 
plt.tight_layout()  
plt.show()
