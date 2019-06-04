class Solution:
    def bubleSort(self,nums):
        if not nums:
            return []
        l = len(nums)-1
        for i in range(l):
            for j in range(l-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums
if __name__ == "__main__":
    nums = [3,6,9,2,3,6,7,4,5,1]
    print(Solution().bubleSort(nums))
