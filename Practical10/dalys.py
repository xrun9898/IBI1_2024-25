import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical10")
print(os.getcwd())
dalys_data = pd.read_csv("C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical10/dalys-rate-from-all-causes.csv")
print(dalys_data.iloc[0:10,2])
print(f"the 10th year with DALYs data recorded in Afghanistan was {dalys_data.iloc[9,2]}. ")
#the 10th year with DALYs data recorded in Afghanistan was 1999
boolean_index = dalys_data['Year'] == 1990  
dalys_1990 = dalys_data.loc[boolean_index, [True,False,False,True ]]  
print(dalys_1990)


uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'bo')
plt.title("DALYs in the UK")
plt.xlabel("Year")  
plt.ylabel("DALYs")

plt.show()
uk.year = uk.Year.astype(str)
uk.DALYs = uk.DALYs.astype(float)
uk_dalys = uk.DALYs.tolist()
ukMean = np.mean(uk_dalys)

fr = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
fr.year = fr.Year.astype(str)
fr.DALYs = fr.DALYs.astype(float)
fr_dalys = fr.DALYs.tolist()
frMean =np.mean(fr_dalys)
print(f"The average DALYs in the UK is {ukMean}, and the average DALYs in France is {frMean}.")
if ukMean > frMean:
    print("The average DALYs in the UK is higher than that in France.")
else:   
    print("The average DALYs in France is higher than that in the UK.")
#The average DALYs in the UK is higher than that in France.

#answer the question
cn = dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
plt.plot(cn.Year, cn.DALYs, 'bo')
plt.title("DALYs in China")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()
less=0
more=0
cn.year = cn.Year.astype(str)
cn.DALYs = cn.DALYs.astype(float)
cn_dalys = cn.DALYs.tolist()
for i in range(len(cn_dalys)-1):
    if cn_dalys[i] > cn_dalys[i+1]:
        less  +=1
    elif cn_dalys[i] < cn_dalys[i+1]:   
        more+=1
print(f"the number of years with a decrease in DALYs is {less}, and the number of years with an increase in DALYs is {more}. \n as a reslut the DALYs in China is decreasing.")
