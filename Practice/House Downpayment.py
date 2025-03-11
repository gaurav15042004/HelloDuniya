price=1000000
print(price)
Good_Credit=input("Do you have good credit?(yes/no) ")
if Good_Credit=="yes":
    downpayment_low=price*0.1
    print(downpayment_low)
else :
    downpayment_high=price*0.2
    print(f"Downpayment is=${downpayment_high}")