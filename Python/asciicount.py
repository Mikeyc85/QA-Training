alpha=[0]*26
msg=input("Enter any message")
for ch in msg:
    alpha[ord(ch)-65]+=1

i=0
while i<len(alpha):
    if alpha[i]!=0:
        print(chr(i+65),";",alpha[i])
    i+=1
