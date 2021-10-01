def tax(salary):
    t=salary*25/100
    return t

salary=int(input("Enter salary here:"))
net=salary-tax(salary)
print("Salary:",salary)
print("Tax:",tax(salary))
print("Net Salary",net)