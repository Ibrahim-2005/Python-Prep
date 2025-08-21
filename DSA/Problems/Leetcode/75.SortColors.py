nums = [2,0,2,1,1,0,2]
# Cannot use sort()
print(nums)
count=[0,0,0]
for i in nums:
    count[i]+=1
R,W,B=count
nums[:R]=[0]*R
nums[R:R+W]=[1]*W
nums[R+W:]=[2]*B
print(nums)