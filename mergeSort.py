class Solution:
    def Sort(self,nums):
        if len(nums) == 1:
            return nums
        mid = (len(nums)//2)
        left = nums[:mid]
        right = nums[mid:]

        l1 = self.Sort(left)
        r1 = self.Sort(right)
        return self.merge(l1,r1)
    def merge(self,left,right):
        result = []
        while len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result+=left
        result+=right

        return result
if __name__ == "__main__":
    nums = [1,9,6,3,8,2,7,4]
    print(Solution().Sort(nums))
