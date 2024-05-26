import random

list_of_options = ["cherry", "banana", "strawberry"]

a = random.choice(list_of_options)
b = random.choice(list_of_options)
c = random.choice(list_of_options)



if a == b == c:
    print("jackpot")
elif a == b or a == c or b == c:
    print("you won the small prize")
else:
    print("you lost")
