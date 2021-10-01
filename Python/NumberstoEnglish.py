def ty(num):
    data=""
    if num==20: data="twenty"
    elif num==30: data="thirty"
    elif num==40: data="forty"
    elif num==50: data="fifty"
    elif num==60: data="sixty"
    elif num==70: data="seventy"
    elif num==80: data="eighty"
    elif num==90: data="ninety"
    return data

def ones(num):
    data=""
    if num==1: data="one"
    elif num==2: data="two"
    elif num==3: data="three"
    elif num==4: data="four"
    elif num==5: data="five"
    elif num==6: data="six"
    elif num==7: data="seven"
    elif num==8: data="eight"
    elif num==9: data="nine"
    elif num==10: data="ten"
    elif num==11: data="eleven"
    elif num==12: data="twelve"
    elif num==13: data="thirteen"
    elif num==14: data="fourteen"
    elif num==15: data="fifteen"
    elif num==16: data="sixteen"
    elif num==17: data="seventeen"
    elif num==18: data="eighteen"
    elif num==19: data="nineteen"
    return data

num=int(input("Enter Any Number:"))
answer=""
if num>=1000:
    answer=ones(int(num/1000)) + " thousand "
    num%=1000
if num>=100:
    answer+=ones(int(num/100)) + " hundred "
    num%=100
if num>=20:
    answer+=ty(int(num/10)*10) + " "
    num%=10
if num>=1:
    answer+=ones(num)

print(answer)