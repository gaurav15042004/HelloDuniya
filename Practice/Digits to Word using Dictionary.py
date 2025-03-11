in_word = {1:"One ",
           2:"Two ",
           3:"Three ",
           4:"Four ",
           5:"Five ",
           6:"Six ",
           7:"Seven ",
           8:"Eight ",
           9:"Nine ",
           0: "zero "
           }
in_digit= input('Enter the Number: ')
output= ""
for number in in_digit:
    number = int(number)
    number = in_word.get(number)
    output += number
print(f"{output}")
