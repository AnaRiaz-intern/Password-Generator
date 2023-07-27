import random
import string


def Generate_Password():
    special_charcter = ''
    digits = ''
    pass_length = random.randint(8, 16)
    Number_of_letters = pass_length
    print("Password Length: ", pass_length, "\n")
    print("Do you want to Include Numbers in your Password?")
    a = str(input("Type Yes or No ---> "))
    if (a == "Yes"):
        digits = (random.randint(10, 100))
        Number_of_letters -= 2
    print("Do you want to Include Spcial Charcaters in your Password?")
    b = str(input("Type Yes or No ---> "))
    if (b == "Yes"):
        special_charcter = random.choice(string.punctuation)
        Number_of_letters -= 1
    letters = random.choices(string.ascii_letters, k=Number_of_letters)
    password = ''.join(letters) + special_charcter + str(digits)
    return password


print("Lets create a Password for You!")
print("----------------------------------------------------\n")
print("Password: ", Generate_Password())
print("----------------------------------------------------\n")
