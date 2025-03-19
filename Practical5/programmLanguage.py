'''define dictionary lang_popularity containing programming languages and their user percentages  
  
  print "Programming Language Popularity:"  
  print contents of lang_popularity  
  
  convert keys() to a list and assign it to languages  
  convert values() to a list and assign it to users_percentage  
  
  use plt.bar to create a bar chart with languages on the x-axis and users_percentage on the y-axis  
  set chart title to 'Programming Language Popularity (Feb 2024)'  
  set x-axis label and y-axis label
  add grid lines to the y-axis  
  
  show the chart  
  
  promot user to input a programming language, assign input to input_language  
  retrieve user percentage from lang_popularity using input_language, return "Language not found!" if not found  
  print "The percentage of developers who use [input_language] is: [percentage]%"  '''


import matplotlib.pyplot as plt  

lang_popularity = {  
    "JavaScript": 62.3,  
    "HTML": 52.9,  
    "Python": 51.0,  
    "SQL": 51.0,  
    "TypeScript": 38.5  
}  

print("Programming Language Popularity:")  
print(lang_popularity)  
 
languages = list(lang_popularity.keys())  
users_percentage = list(lang_popularity.values())  

plt.bar(languages, users_percentage, color='skyblue')  
plt.title('Programming Language Popularity (Feb 2024)')  
plt.xlabel('Languages')  
plt.ylabel('Users (%)')  
plt.grid(axis='y')  

plt.show()  

input_language =input("想查的语言")   
percentage = lang_popularity.get(input_language, "Language not found!")  
print(f"The percentage of developers who use {input_language} is: {percentage}%") 