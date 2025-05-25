print("please input your age weight and dosage in one line, which  are splited by spaces  ")
datas= input("input the datas").split()
def calculator(datas) :
    try :
        age = int(datas[0])
        weight = int(datas[1])
    except ValueError:  
        return "Please ensure that age and weight are entered as numbers and are correct."
    if age >18:
        print('age should be below 18 years')
    if weight<=0 or weight>=100 or datas[2] !=  "120mg/5ml" and datas[2] != "250mg/5ml" :
        return "The drug concentration should be '120mg/5ml' or '250mg/5ml'. Please enter a valid weight within the range of 1 to 99 kilograms."
    if datas[2] =="120mg/5ml" :
        drug = weight *15/120*5
        return drug
    else :
        drug = weight *15/250*5
        return drug
print(calculator(datas))                    

#example output
# please input your age weight and dosage in one line, which  are splited by spaces
# input the datas 18 50 120mg/5ml
# 18