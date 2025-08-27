def selection_sort(nums):
    n=len(nums)

    for i in range(n):
        min_idx=i
        j=i+1
        while j<n:
            if nums[i]>nums[j]:
                min_idx=j
            nums[i],nums[min_idx]=nums[min_idx],nums[i]
            j+=1
    return nums


    # for i in range(n):
    #     min_idx=i
    #     for j in range(i+1,n):
    #         if nums[i]>nums[j]:
    #             min_idx=j
    #     nums[i],nums[min_idx]=nums[min_idx],nums[i]
    # return nums



nums=[2,4,6,7,-3,-6,-9]
print(selection_sort(nums))