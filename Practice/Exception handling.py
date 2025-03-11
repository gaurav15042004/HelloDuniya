try:
    age = int(input("what's your age? "))
    print(age)
    income= int(input("what's your income? "))
    risk= income/age
    print(f"Your risk factor is {risk}")

except ValueError:
    print("Sorry, I didn't understand that.")

except ZeroDivisionError:
    print("Age cannot be zero!")
