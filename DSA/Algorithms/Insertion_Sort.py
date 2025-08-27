def insertion_sort(nums):
    n=len(nums)
    # for i in range(1,n):
    #     j=i
    #     while(j>0 and nums[j-1]>nums[j]):
    #         nums[j-1],nums[j]=nums[j],nums[j-1]
    #         j-=1
    # return nums

    for i in range(1,n):
        for j in range(i,-1,-1):
            if nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
    return nums


nums=[2,4,6,7,-3,-6,-9]
print(insertion_sort(nums))