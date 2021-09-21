nums = [21,35,34,38,390,47,56,47,58,558,2221,21,320,20,21,223,32,654,64,67,99,980,451]

highest=nums[0]
i=1
while i<len(nums):
    if nums[i]>highest:
        highest=nums[i]
    i=i+1

print (highest)
