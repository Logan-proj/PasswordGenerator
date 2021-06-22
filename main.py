#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nPython Password Generator")
print("-------------------------")

def password_generator():
  password_length = int(input("Enter charachter length: "))

  password_list = []

  #Desired amount of symbols & numbers <= 40% of string
  numberchar = int(password_length * .2)
  symbolchar = int(password_length * .2)

  #Randomly choosing & adding numbers to list
  for char in range(random.randint(1, numberchar)):
    password_list.append(random.choice(numbers))

  #Randomly choosing & adding symbols to list
  for char in range(random.randint(1, symbolchar)):
    password_list.append(random.choice(symbols))

  #How many letters are needed to meet password length requirement
  letter_length = (password_length - len(password_list))

  #Add random letters to end of password list
  password_list.extend(random.choices(letters, k=letter_length))

  random.shuffle(password_list)

  #Turn list into string
  password = ""
  for char in password_list:
    password += char

  print(f"Your generated password: {password}")

run_program = True
while run_program:
  password_generator()
  result = input("\nRun program again? Type Y for yes or N for no: ").lower()
  if result == "n":
    run_program = False
    print("\nGoodbye")
