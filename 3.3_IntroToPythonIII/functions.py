#Basic Definition
def name(parameters):
    #code goes here
    return

#simple function with no parameters
def show():
        print(f"HI!")

#Use parenthesis to run the code in a function
show()

#Simple function with one parameter
def show(message):
        print(message)

#think of the parameter 'message' as a variable
#you assign the string "Hello, World!" when you call the function
#This is like saying 'message="Hello, World!"'
show("Hellow, World!")

#Functions can have more than one parameter
def make_quesadilla(protein, toopping)
    quesadilla=f'Here is a {protein} queadilla with {topping}.'
    print(quesadilla)

#supply the arguments when calling the function
make_quesadilla["beef","sour cream"]

#Note: Order is important when suppolying arguments
make_quesadilla("sour cream","beef")

#we can also specify default values for parrementers
def make_quesadilla(protein, topping="sour cream"):
        quesadilla=f'Here is a {protein} quesadilla with {topping}'
        print(quesadilla)

#make a quesadilla using the default topping
make_quesadilla("chicken")

#make a quesadilla with a new topping
make_quesadilla("chicken", "guacamole")

#Fuctions can return a value
def square(number):
    return number*number

#you can save the value that is
squared=square(2)
print(squared)

#You can also just print the returned value
print(square(2))
print(square(3))
