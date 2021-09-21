salary = int (input("Enter your salary:"))

if salary >=2000:
    tax=salary*25/100

if salary <2000:
    tax=salary*15/100

net=salary-tax
print("Your Salary:", salary)
print("Your Tax:", tax)
print("Net Salary:",net)
