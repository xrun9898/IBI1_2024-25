'''
input: weight, height
bmi=weight/(height/100)**2
if bmi<18.5: Underweight
elif bmi<=30: Normal
elif bmi>30: Obesity
ouput: bmi, status'''

weight=int(input("weight?"))
height=int(input("height?"))
bmi=weight/(height/100)**2
if bmi<18.5:
    print(str(bmi)+" Underweight")
elif bmi<=30:
    print(str(bmi)+" Normal")
elif bmi>30:
    print(str(bmi)+" Obesity")