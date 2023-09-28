FullName = input(str("Enter Your Full Name: "))
Shop = input(str("Enter shop name: "))
Item = input(str("Enter item Name: "))
Purchase = eval(input("Enter purchase amount:  "))
Tax = (Purchase * 0.06 )
print()
print("Name:", FullName)
print("The Shop Name is ", Shop)
print("The Item Name is", Item)

print("The Sales Tax is ", round(Tax, 2))



