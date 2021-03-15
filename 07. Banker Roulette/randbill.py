import  random
strname = input("Enter everyones name separated by a comma ").split(", ")
#name = strname.split(", ")
person_who_will_pay = random.choice(strname)
# num_elements = len(name)
# random_num = random.randint(0,num_elements - 1)
# print(random_num)
# person_who_will_pay = name[random_num]
print(person_who_will_pay, "will pay the bill")