menu = {
  'Tea':50,
  'Coffee':145,
  'Pizza':450,
  'MoMO':120,
  'Burger':450,
}
print("wellcome to our hotel")
print(" Tea:50 \n Coffee:14 \n Pizza:450 \n MoMO:120 \n Burger:450")
total=0
a=input("Enter name of item you want to order\n")
if a in menu:
    total=total+menu[a]
    print(f"Your order {a} has neen added")
else:
    print(f"Ordered item {a} not available yet")    
b = input("Do you want do add another order?\n(yes|no)\n")  
if b =="yes":
    a2=input("Enter name of second item you want to order\n")
    if a2 in menu:
        total = total+menu[a2] 
        print(f"Your order {a2} has neen added")
    else:
        print(f"Ordered item {a2} not available yet")  
print(f"The order amount is {total}")

    