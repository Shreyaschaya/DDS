class Solution:
    def pivotIndex(self, nums: List[int]) ->int:
        t= sum(nums)
        lt=0
        for i in range (len(nums)):
            rt = t-lt-nums[i]
            if rt == lt:
                return i
            lt += nums[i]
        return -1
