class Solution:
    def find(self,nums,target,start,end):
        mid = start+(target-nums[start])//(nums[end]-nums[start])*(end-start)
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            return self.find(nums,target,start,mid-1)
        if nums[mid]<target:
            return self.find(nums,target,mid+1,end)

if __name__ == "__main__":
    nums = [5,6,7,8,9,10,11,12]
    target=6
    print(Solution().find(nums,target,0,len(nums)-1))
