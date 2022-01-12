import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letterLength = len(letters)
numberLength = len(numbers)
symbolLength = len(symbols)
genlet = str()
gensym = str()
gennum = str()
for i in range(0,nr_letters):
  genl = random.randint(0,letterLength-1)
  genle = letters[genl]
  genlet = genle + genlet
for i in range(0,nr_symbols):
  gens = random.randint(0,symbolLength-1)
  gensy = symbols[gens]
  gensym = gensy + gensym
for i in range(0,nr_numbers):
  genn = random.randint(0,numberLength-1)
  gennu = numbers[genn]
  gennum = gennu + gennum

password =[]
genPassword = str(genlet + gensym + gennum)
for x in genPassword:
  password.append(x)
random.shuffle(password)
randomPassword =str()
for i in password:
  randomPassword += i
print(f"Your generated password is {randomPassword}")