def count_vowels(username):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in username:
        if ch in vowels:
            count += 1

    print("Number of vowels in username is:", count)
user = input("Enter your username: ")
count_vowels(user)