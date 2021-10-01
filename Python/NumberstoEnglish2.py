ty=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

num=int(input("Enter Any Number:"))
answer=""
if num>=1000:
    answer=ones[int(num/1000)] + " thousand "
    num%=1000
if num>=100:
    answer+=ones[int(num/100)] + " hundred "
    num%=100
if num>=20:
    answer+=ty[int(num/10)] + " "
    num%=10
if num>=1:
    answer+=ones[num]

print(answer)