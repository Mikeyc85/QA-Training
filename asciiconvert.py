alpha=input("Enter Any Character:")

if ord(alpha)>=65 and ord(alpha)<=90:
    print(chr(ord(alpha)+32))

if ord(alpha)>=90 and ord(alpha)<=122:
    print(chr(ord(alpha)-32))