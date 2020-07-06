age = 17
if age >= 18:
    print("You are ord enough")
    print("Have")
else:
    print("Sorry, you are too young")
    print("Please")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("You " + str(price) + " .")

resquested_toppings = []
if resquested_toppings:
    print("!")
else:
    print("?")
