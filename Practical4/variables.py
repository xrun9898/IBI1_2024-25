a=15
b=75
c=a+b
d=90
e=5
f=d+e
if c>f:
    print("f is longer,c is faster")
else:
    print("c is longer,f is faster")

x = True
y = False
w = x and y
print("w:",w)
'''
Truth table for w (x and y)
| x     | y     | w (x and y) | x or y 
| True  | True  | True        | True
| True  | False | False       | True
| False | True  | False       | True
| False | False | False       | False
'''