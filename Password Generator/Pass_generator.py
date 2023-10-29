import string
import random

p1 = list(string.ascii_lowercase)
p2 = list(string.ascii_uppercase)
p3 = list(string.digits)
p4 = list(string.punctuation)

pass_length = input("How many characters do you want in your password? ")

while True:
    try:
        characters_number = int(pass_length)
        if characters_number < 8:
            print("Your number should be at least 8.")
            pass_length = input("Please, Enter your number again: ")

        else:
            break

    except:
        pass_length = input("How many characters do you want in your password: ")

random.shuffle(p1)
random.shuffle(p2)
random.shuffle(p3)
random.shuffle(p4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

result = []

for x in range(part1):

    result.append(p1[x])
    result.append(p2[x])

for x in range(part2):

    result.append(p3[x])
    result.append(p4[x])

random.shuffle(result)

password = "".join(result)
print("Password: ", password)