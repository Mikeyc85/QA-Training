product = input("Enter the name of the product:")
quantity= input("Enter the quantity:")
price= input ("Enter the unit price:")
bill= int(quantity) *float(price)
print ("Your bill details are.....")
print ("You bought:", product)
print ("Quantity:",quantity)
print ("Price:", price)
print ("--------------")
print("your bill is: £",bill)
print ("--------------")