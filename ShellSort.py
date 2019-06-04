class Solution:
    def Sort(self,nums):
        if not nums:
            return []
        n = len(nums)
        gap = n//2
        while gap>0:
            for i in range(gap,n):
                for j in range(i,gap-1,-gap):
                    if nums[j]<nums[j-gap]:
                        nums[j],nums[j-gap]=nums[j-gap],nums[j]
                    else:
                        break
            gap//=2
        return nums
if __name__ == "__main__":
    nums = [1,9,6,3,8,2,7,4]
    print(Solution().Sort(nums))
