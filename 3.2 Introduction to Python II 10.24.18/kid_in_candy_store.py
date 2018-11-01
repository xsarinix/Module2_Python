# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

print(f"Your allowance is {allowance} candies.")

choice=0
while allowance>0:
    choice=input("Pick a candy between 0 and "+str(candyList.index(candy))+". ")
    candyCart.append(candylist.index(choice))
    print(f"You've added {candylist.index(choice)} to your cart.")
    allowance=allowance-1
    print(f"Your remaining candy allowance is {allowance}.")    

print(f"You put the following candies in your cart.")
for candy in candyCart:
        print(candy)    


