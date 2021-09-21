bill=int(input("Enter the bill:"))
paid=int(input("Enter paid:"))
balance=paid-bill
if balance >=50:
    fifty=int(balance/50)
    print ("50 pounds:", fifty)
    balance=balance-(fifty*50)
if balance >=20:
    twenty=int(balance/20)
    print ("20 pounds:",twenty)
    balance=balance-(twenty*20)
if balance >=10:
    print ("10 pounds:", 1)
    balance=balance-int(10)
if balance >=5:
    print ("5 pounds:", 1)
    balance=balance-int(5)
if balance >=2:
    two=int(balance/2)
    print ("2 pounds:",two)
    balance=balance-(two*2)
if balance >=1:
    print ("1 pound:", 1)
    balance=balance-int(1)
print ("Remaining balance is", balance)