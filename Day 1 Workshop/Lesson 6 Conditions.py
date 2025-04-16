#Example 1
Mark = int(input("Enter your mark: "))

#This is the starting condition
if Mark >= 75:
    print(f"You have passed with a distinction, with the mark of {Mark}")

#This are additional conditions if the starting condition is not met
elif Mark >= 50:
    print(f"You have passed, with the mark of {Mark}")

elif Mark >= 40:
    print(f"You have passed, with the mark of {Mark}. But you need to do supps")

#This is the final condition if all the above conditions are not met
else:
    print(f"You have failed, with the mark of {Mark}")

#Example 2
Raffle = int(input("Enter your raffle number: "))

if Raffle == 100:
    print('You won the raffle!!')
else:
    print('You did not win the raffle!!')

#Example 3
daysoftheweek = input("Enter the day of the week: ")

match daysoftheweek:
    case 'monday':
        print("Enjoy your monday")

    case 'tuesday':
        print("Enjoy your tuesday")

    case _:
        print("We do not have that day")

#Example 4
name = "Name"
age = 22

if name == "Name":
    if age >= 22:
        print(f"You are {name} and you are {age} years old")