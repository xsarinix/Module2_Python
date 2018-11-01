# To-Do: Write a function that returns the arithmetic average for a list of numbers

def avg(num_list):
    length=len(num_list)
    total=0.00
    for value in num_list:
        total+=value
    return total/length

# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))

average=[1,5,9]
print(avg(average))

average=list(range(11))
print(avg(average))
