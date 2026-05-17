def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
n = int(input("Enter a number: "))
even_odd(n)