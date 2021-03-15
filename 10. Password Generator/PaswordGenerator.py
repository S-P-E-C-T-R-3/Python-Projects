import random
print("************Welcome to Password Generartor***********")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')']
num_letters = int(input("How many letters u want in ur paasword "))
num_symbols = int(input("How many symbols u want in ur password "))
num_numbers = int(input("How many numbers u want in ur password "))

#ez Mode
# pswrd_generated = ""
#
# if num_letters >
# for char in range(1,num_letters + 1):
#     pswrd_generated += random.choice(letters)
# print(pswrd_generated)
#
# for char in range(1,num_symbols + 1):
#     pswrd_generated += random.choice(symbols)
# print(pswrd_generated)
#
# for char in range(1,num_numbers + 1):
#     pswrd_generated += random.choice(numbers)
# print(pswrd_generated)

#hard Mode
pswrd_generated = []

for char in range(1,num_letters + 1):
    pswrd_generated.append(random.choice(letters))

for char in range(1,num_symbols + 1):
    pswrd_generated.append(random.choice(symbols))

for char in range(1,num_numbers + 1):
    pswrd_generated.append(random.choice(numbers))
print(pswrd_generated)
random.shuffle(pswrd_generated)
print(pswrd_generated)

pswrd_to_string = ""
for char in pswrd_generated:
    pswrd_to_string +=char
print("Your Generated Password is "+pswrd_to_string)
