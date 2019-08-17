#非递归
class Solution:
    def find(self,nums,target):
        if not nums:
            return False
        nums.sort()
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        return False

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7]
    target=5
    print(Solution().find(nums,target))

#递归
class Solution:
    def find(self,nums,target,start,end):
        mid = start+(end-start)//2
        if start>end:
            return False
        if nums[mid]>target:
            end = mid-1
        elif nums[mid]<target:
            start = mid+1
        else:
            return True
        return self.find(nums,target,start,end)

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7]
    target=6
    print(Solution().find(nums,target,0,len(nums)-1))
