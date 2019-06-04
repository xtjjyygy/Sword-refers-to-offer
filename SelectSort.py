class Solution:
    def SelectSort(self,nums):
        if not nums:
            return []
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
            #print("roud"+str(i),nums)
        return nums
if __name__ == "__main__":
    nums = [3,6,9,2,3,6,7,4,5,1]
    print(Solution().SelectSort(nums))
