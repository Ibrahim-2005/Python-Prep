nums = [2,7,11,15,5,6,7,9]
target = 11
hashmap={}
for i,v in enumerate(nums):
    if target-v in hashmap:
        print(i,hashmap[target-v])
        break
    else:
        hashmap[v]=i


i=0
for j in range(1,len(nums)):
    if nums[i]+nums[j]==target:
        print(i,j)
    i+=1