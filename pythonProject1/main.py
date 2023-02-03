# Rollercoaster ticketing Exercise

welcome = "Welcome to zte "
height = int(input("Please enter your height in meters: "))
if height < 120:
    print("You are not tall enough to take this ride :-(")
    exit()
age = int(input("Please enter your age: "))
if age > 50:
    print("Sorry your too old to take this ride")
    exit()
elif age >= 18:
    print("Would you like to take a photo for an extra 1,000? Enter Y or N")
    pic = input("")
    if pic == "Y" or "y":
        print(welcome + "your total is 6,000")
    else:
        print(welcome + "your total is 5,000")
elif age > 13 <= 17:
    print("Would you like to take a photo for an extra 1,000? Enter Y or N")
    pic = input("")
    if pic == "Y" or "y":
        print(welcome + "your total is 4,000")
    else:
        print(welcome + "your total is 3,000")
elif age >= 12 < 14:
    print("Would you like to take a photo for an extra 1,000? Enter Y or N")
    pic = input("")
    if pic == "Y" or "y":
        print(welcome + "your total is 3,000")
    else:
        print(welcome + "your total is 2,000")
else:
    print("You are not legible to take this ride")
