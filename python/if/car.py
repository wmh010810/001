cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
resquested_topping = 'mushrooms'
if resquested_topping != 'anchovies':
    print("Hold the anchovies!")
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish. ")
