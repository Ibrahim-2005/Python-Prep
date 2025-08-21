nums=[1,2,3,4,5]

result=[nums[0]]

for i in range(len(nums)-1):
    result.append(result[i]+nums[i+1])
print(result)
