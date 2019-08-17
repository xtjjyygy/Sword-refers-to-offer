class Solution:
    def find(self,nums,target,start,end):
        if start>end:
            return False
        mid = start+(target-nums[start])//(nums[end]-nums[start])*(end-start)
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            end = mid-1
        if nums[mid]<target:
            start = mid+1
        return self.find(nums,target,start,end)

if __name__ == "__main__":
    nums = [5,6,7,8,9,10,11,12]
    target=10
    print(Solution().find(nums,target,0,len(nums)-1))
