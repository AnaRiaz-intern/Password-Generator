import random
import string


def Generate_Password():
    pass_length = random.randint(8, 16)
    print("Length: ", pass_length, "\n")
    letters = random.choices(string.ascii_letters, k=pass_length-2)
    special_charcter = random.choice(string.punctuation)
    digits = (random.randint(10, 100))
    password = ''.join(letters) + special_charcter + str(digits)
    return password 


print("Your Password Details:")
print("--------------------------\n")
print("Password: ", Generate_Password())
print("--------------------------\n")
