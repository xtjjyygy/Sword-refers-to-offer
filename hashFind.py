class Solution:
    def find(self, nums, target):
        if not nums:
            return False
        lookup = {}
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = i
            else:
                continue
        for i in lookup.keys():
            if i == target:
                return lookup[i]


if __name__ == "__main__":
    nums = [3, 1, 8, 5, 3, 9, 0]
    target = 8
    print(Solution().find(nums, target))
