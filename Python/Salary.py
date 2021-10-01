name=input("Enter Employee's Name:")
salary=input("Enter Employee's Salary:")
tax = int(salary)*20/100
net = int(salary)-tax
print ("Salary Slip.....")
print ("Employee's Name:", name)
print (name,"'s", "Salary is", salary)
print ("Tax", tax)
print ("Net Salary:", net)