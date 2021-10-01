msg=input("Enter any message:")
i=0
word=""
while i<len(msg):
    if msg[i]==" ":
        print(word)
        word=""
    else:
        word=word+msg[i]
    i=i+1
print (word)
reversed