# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
created_string = ""
created_symbol_string = ""
created_number_string = ""


for i in range(0, nr_letters + 1):
    random_number = random.randint(0, len(letters))
    created_string += letters[random_number]


for x in range(0, nr_symbols):

    random_number = random.randint(0, nr_symbols)
    created_symbol_string += symbols[random_number]

for y in range(0, nr_numbers):
    random_number = random.randint(0, nr_numbers)
    created_number_string += str(numbers[random_number])

created_password = created_string + created_symbol_string + created_number_string
print("Here is Your Weak Password: ", created_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_created_password = []
for char in created_password:
    random_number = random.randint(0, len(created_password))
    random_created_password.extend([char])


random.shuffle(random_created_password)


strong_password = ""
for chars in random_created_password:
    strong_password += chars
print("Here is your strong password", strong_password)
