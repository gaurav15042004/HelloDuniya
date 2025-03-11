element= input("enter element separated by ','--> ")
list= element.split(",")

unique_list=[]
for number in list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)