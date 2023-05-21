import random

print("Welcome to slots")

# list of fruits
fruits = ("Apple", "Cherry", "Lemon")

# picks a random fruit from the list
fruit1 = random.choice(fruits)
fruit2 = random.choice(fruits)
fruit3 = random.choice(fruits)

# prints the fruits
print(fruit1, fruit2, fruit3)

# Checks if they are all the same
if fruit1 == fruit2 == fruit3:
    print("Congratulations You Won!")
else:
    print("Oh no you lost")
