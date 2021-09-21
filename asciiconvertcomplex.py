newmsg=""
msg=input("Enter Any Messsage:")

for ch in msg:
    if ord(ch)>=65 and ord (ch)<=90:
        newmsg+=chr(ord(ch)+32)
    elif ord(ch)>=97 and ord (ch)<=122:
        newmsg+=chr(ord(ch)-32)
    elif ord(ch)>=48 and ord (ch)<=57:
        newmsg+= str(int(ch)*2)
    else:
        newmsg+=ch
    
print(newmsg)