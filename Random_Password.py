import random
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', '/', '|']

print("Welcome👋,This Is The Random Password Generator🤫 ! ")
num_Small_letters = int(input("How Many Small Letters Do You Want In Your Password❓\n"))
num_Capital_letters = int(input("How Many Capital Letters Do You Want In Your Password❓\n"))
num_Numbers = int(input("How Many Numbers Do You Want In Your Password❓\n"))
num_Symbols = int(input("How Many Symbols Do You Want In Your Password❓\n"))

password = []

for i in range(1, num_Small_letters + 1):
    password.append(random.choice(small_letters))

for i in range(1, num_Capital_letters + 1):
    password.append(random.choice(capital_letters))

for i in range(1, num_Numbers + 1):
    password.append(random.choice(numbers))

for i in range(1, num_Symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
password = "".join(password)

print(f"Your Password Is [Please Don't Share It🤫🤫] : {password} \n")