''' Define population data for UK countries (in millions)  
    Define population data for Zhejiang neighboring provinces (in millions)  
    Sort the populations  
    set sorted_uk_population = SORT(uk_countries)  
    set sorted_china_population = SORT(zhejiang_neighboring_provinces)  

    Print sorted populations  
    print "sorted UK populations and sorted China neighboring provinces populations

    set labels for the pie charts  
    set labels_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']  
    set labels_china = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']  

    create a figure for the pie charts  with size (12, 6)  
    pie chart for UK countries  
    set subplot to (1, 2, 1)  
    create pie chart using uk_countries with labels_uk
    set title 
    using the same method to create the pie chart of chinese provinces 

    adjust layout for better presentation and tightness  
    display the charts  '''  

import matplotlib.pyplot as plt  

uk_countries = [57.11, 3.13, 1.91, 5.45]  
zhejiang_neighboring_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]  
sorted_uk_population = sorted(uk_countries)  
sorted_china_population = sorted(zhejiang_neighboring_provinces)  

print("Sorted UK populations (millions):", sorted_uk_population)  
print("Sorted China neighboring provinces populations (millions):", sorted_china_population)  
 
labels_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']  
labels_china = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']  
  
plt.figure(figsize=(12, 6))  

plt.subplot(1,2,  1)  
plt.pie(uk_countries, labels=labels_uk, autopct='%1.1f%%', startangle=140,)  
plt.title('Population Distribution of UK Countries (2022)')  

plt.subplot(1, 2, 2)  
plt.pie(zhejiang_neighboring_provinces, labels=labels_china, autopct='%1.1f%%', startangle=140)  
plt.title('Population Distribution of Zhejiang Neighboring Provinces (2022)')  

plt.tight_layout()  
plt.show()