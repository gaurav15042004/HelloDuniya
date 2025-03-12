def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return ("Fizzbuzz")
    elif input % 3 ==0:
        return ("Fizz")
    elif input % 5 == 0:
        return ("Buzz")
    else:
        return input


output = fizz_buzz(int(input()))
print(output)
