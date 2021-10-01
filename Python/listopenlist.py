nums=[]
number=1

while number!=0:
    number=int(input("Enter any number:"))
    if number!=0:
        nums.append(number)

i=0
high=nums[0]

while i<len(nums):
    if nums[i]>high:
        high=nums[i]
    i=i+1

print("the biggest number entered was:", high)