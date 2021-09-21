msg=input("Enter any message:")
count=0
i=0
while i<len(msg):
    if msg[i]==" ":
        count=count+1
    i=i+1
if count==0:
    print ("you entered",count+1,"word")
else:
    print("you entered", count+1,"words")