class Solution:
    def InsertSort(self,nums):
        if not nums:
            return []
        l = len(nums)
        for i in range(1,l):
            j = i-1
            if nums[i]<nums[j]:
                temp = nums[i]
                nums[i]=nums[j]

                j=j-1
                while j>=0 and nums[j]>temp:
                    nums[j+1]=nums[j]
                    j-=1
                nums[j+1]=temp
        return nums
if __name__ == "__main__":
    nums = [5,3,7,2,9,3,0,1]
    print(Solution().InsertSort(nums))
