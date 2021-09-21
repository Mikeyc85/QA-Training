def tax(name,salary):
    if salary>=2000:
        t=salary*25/100
    else:
        t=salary*15/100
    net=salary-t
    print("Salary slip of name",name,"---------------")
    print("Employee name:",name)
    print("Employee Salary:", salary)
    print("Tax:",t)
    print("Net Salary:", net)


n=input("Employee name here:")
s=int(input("Salary:"))
tax (n,s)