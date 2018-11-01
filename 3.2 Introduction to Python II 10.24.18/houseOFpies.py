order_status="yes"
order_total=0
pie_cart=[]
print("Welcome to the House of Pies! Here are our pies:")
print()
print("------------------------------------------------")
print()
pie_list=["Pecan","Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
pie_count=0
for pie in pie_list:
    pie_count=pie_count+1
    print("("+str(pie_count)+") "+pie)
print()
while order_status=="yes":
    pie_num=int(input("Which pie would you like to bring home? Enter a number 1 to "+str(pie_count)+". "))
    pie_index=pie_num-1
    #order_total=order_total+1
    pie_cart.append(pie_list[pie_index])
    print()
    print("Great! We'll have that "+pie_list[pie_index]+" Pie right out for you!")
    order_status=input("Would you like to get another pie? (yes or no) ")
# print("You have ordered a total of "+str(order_total)+" pies. Thank you for visiting the House of Pies!")
print()
print("You ordered the following pies: ")
print(pie_cart)
print("You have ordered a total of "+str(len(pie_cart))+" pies.")


    