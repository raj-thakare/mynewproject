def multiple_of_five(num):
    if num % 5 == 0:
        print(num, "is a multiple of 5")
    else:
        print(num, "is not a multiple of 5")
n = int(input("Enter a number: "))
multiple_of_five(n)