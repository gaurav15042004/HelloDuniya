import math
limit = int(input("Enter a Limit: "))
y=1
while y<limit:
    x=('')
    if y%1==0:
        x=y
        y+=1
    elif y%2!=1:
        x=y
        y+=1
    print (x)
