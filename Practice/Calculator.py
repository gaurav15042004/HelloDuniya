x= float(input("Enter a number: "))
y= float(input("Enter another number: "))
operation = input("Enter operation(+,-,*,/): ")
if operation == "+":
    z = x + y
elif operation== "-":
    z = x - y
elif operation == "*":
    z = x * y
elif operation == "/":
    z = x / y
print(z)