import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numberOfLetter = int(input("How many letters would you like in your password?\n"))
numberOfSymbols = int(input("How many symbols would you like to have?\n"))
numberOfNumbers = int(input("How many numbers would you like?\n"))

password = []

for x in range(1, numberOfLetter + 1):
    password += random.choice(letters)

for x in range(1, numberOfNumbers + 1):
    password += random.choice(numbers)

for x in range(1, numberOfSymbols + 1):
    password += random.choice(symbols)

random.shuffle(password)

strPass = ""

for x in password:
    strPass += x

print(f"Your password is {strPass}")