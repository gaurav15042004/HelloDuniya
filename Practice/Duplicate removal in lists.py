list_1=[1,1,1,2,3,4,5,3,2,1,3,5,6]
unique_list=[]
for number in list_1:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)