weight= input("What's your weight? ")
lbs_or_kg = input("Lbs(L) or kg(k)? ")
if lbs_or_kg == "L"or lbs_or_kg == "l":
    print(f"Your Weight in Kilograms is {float(weight)*0.45}!!!")
elif lbs_or_kg == "k" or lbs_or_kg == "K":
    print(f"Your Weight in Pounds is {float(weight)/0.45}!!!")