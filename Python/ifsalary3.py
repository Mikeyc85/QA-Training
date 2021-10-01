salary = float (input("Enter your salary:"))

if salary >=1000:
    if salary >=2000:
        tax=salary*25/100
    else:
        tax=salary*15/100
else: tax=0
net=salary-tax
print("Your Salary:", salary)
print("Your Tax:", tax)
print("Net Salary:",net)
