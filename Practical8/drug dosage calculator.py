datas = input("input the datas").split()
def calculator(datas) :
    try :
        weight = int(datas[0])
    except ValueError:  
        return "please input valid weight"
    if weight<=0 or weight>=100 or datas[1] !=  "120mg/5ml" and datas[1] != " 250mg/5ml" :
        return "please input correct form datas"
    if datas[1] =="120mg/5ml" :
        drug = weight *15/120*5
        return drug
    else :
        drug = weight *15/250*5
        return drug
print(calculator(datas))