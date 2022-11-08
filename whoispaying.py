import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

names_count = len(names) - 1
random_name = random.randint(0, names_count)
selec_person = names[random_name]
print(f"{selec_person} is going to buy meal today")
