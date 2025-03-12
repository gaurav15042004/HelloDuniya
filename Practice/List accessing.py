def even():
    num = list(range(21))
    even_num = num [::2]
    print(even_num)


def odd():
    num = list(range(21))
    odd_num = num[1::2]
    print(odd_num)


def big():
    big_list = [1,2,3,4,5,6,7,8,9]
    first, second, *other = big_list
    print(first, second)

print('''Hey!!!"
Enter 'even' to see even numbers,
Enter 'odd' to see odd numbers,
Enter 'big' to access only the first and the second number from a big list''')
input = input("Enter your choice: ")


def main():
    if input == "even":
        even()
    elif input == "odd":
        odd()
    elif input == "big":
        big()
    else:
        print("Invalid input")


main()
